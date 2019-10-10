
import pyqtgraph as QtGraph
from pyqtgraph.Qt import QtCore

from collections import deque

QtGraph.setConfigOption('background', 'w')
QtGraph.setConfigOption('foreground', 0.3)

# This class is run off a QT timer. That timer fires and calls the update function
class LivePlotWidget(QtGraph.PlotWidget):
  DEFAULT_PEN_COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

  sigRedraw = QtCore.pyqtSignal()

  def __init__(self, nchan=1, tstep=1.0, history=10.0, init_val=0, fps=30, **kwargs):
    super(LivePlotWidget, self).__init__(**kwargs)
    if self.parent() is None:
      #We are the top level window
      self.setGeometry(0, 0, 800, 600)
      self.setWindowTitle('Stream Plot')

    self.tstep = tstep
    self.tlatest = 0
    self.tmarker = tstep
    self.history = history

    max_samples = int(round(history/tstep)) + 1
    self.nchan = nchan
    self.data = [deque([init_val], maxlen=max_samples) for _ in range(nchan)]
    self.time = deque([0.0], maxlen=max_samples)

    self.curves =[None] * nchan
    for chan in range(nchan):
      pen_color = self.DEFAULT_PEN_COLORS[chan % len(self.DEFAULT_PEN_COLORS)]
      self.curves[chan] = self.plot(self.time, self.data[chan], pen=QtGraph.mkPen(pen_color, width=2))

    self.enableAutoRange(axis=QtGraph.ViewBox.YAxis)
    self.setXRange(-history, tstep, padding=0)
    self.showGrid(True, True)

    self.timer = QtCore.QTimer(self)
    self.timer.setInterval(1000.0/fps)
    self.timer.timeout.connect(self.redraw)

    self.scene().sigMouseClicked.connect(self.onMouseClicked)

  def show(self):
    QtGraph.PlotWidget.show(self)
    self.timer.start()

  def keyPressEvent(self, evt):
    QtGraph.PlotWidget.keyPressEvent(self, evt)
    if evt.text() == 'y':
      self.enableAutoRange(axis=QtGraph.ViewBox.YAxis)
    elif evt.text() == 'x':
      self.enableAutoRange(axis=QtGraph.ViewBox.XAxis)
    elif evt.text() == 'a':
      self.setXRange(self.tmarker - self.history + self.tstep, self.tmarker + self.tstep, 0)

  def onMouseClicked(self, evt):
    if evt.double():
      self.redraw(True)

  #Use the pyQt decorator here to reduce memory and improve performance
  @QtCore.pyqtSlot(list, name='onDataReady')
  def onDataReady(self, data):
    print(data)
    # Loop until the queue is empty
    self.tlatest += self.tstep
    self.time.append(self.tlatest)
    for (chan,datum) in enumerate(data):
      self.data[chan].append(datum)

  #Use the pyQt decorator here to reduce memory and improve performance
  @QtCore.pyqtSlot(name='redraw')
  def redraw(self, force_latest=False):
    # Update the plot
    prev_marker = self.tmarker
    self.tmarker = self.time[-1]
    trange = self.viewRange()[0]
    if (trange[1] >= prev_marker) or force_latest:
      twidth = trange[1] - trange[0]
      if (twidth > self.history):
        twidth = self.history
      self.setXRange(self.tmarker - twidth + self.tstep, self.tmarker + self.tstep, padding=0)
    downsample = (len(self.time) > 2)
    for chan in range(self.nchan):
      self.curves[chan].setData(self.time, self.data[chan], clipToView=True, autoDownsample=downsample, downsampleMethod='subsample')
    self.sigRedraw.emit()