
import numpy as np
import pyqtgraph as QtGraph
from pyqtgraph.Qt import QtCore

from circularbuffer import CircularBuffer

QtGraph.setConfigOption('background', 'w')
QtGraph.setConfigOption('foreground', 0.3)

# This class is run off a QT timer. That timer fires and calls the update function
class LivePlotWidget(QtGraph.PlotWidget):
  DEFAULT_PEN_COLORS = ('b', 'g', 'r', 'c', 'm', 'k')

  sigRedraw = QtCore.pyqtSignal()

  def __init__(self, nchan=1, sample_freq=1.0, buffer_secs=10.0, init_value=None, fps=30,
      title="Stream Plot", **kwargs):
    super(LivePlotWidget, self).__init__(**kwargs)
    if self.parent() is None:
      #We are the top level window
      self.setGeometry(0, 0, 800, 600)
      self.setWindowTitle(title)

    self._sample_period = 1.0/sample_freq
    self._last_redraw_time = 0.0
    self._buf_capacity = int(round(buffer_secs / self._sample_period)) + 1
    self._snap_to_latest = True

    self._nchan = nchan
    self._data = [CircularBuffer(self._buf_capacity, init_value=init_value) for _ in range(nchan)]
    self._time = self._sample_period * (np.arange(self._buf_capacity) - self._buf_capacity - 1)

    self._legend = self.getPlotItem().addLegend()
    self._curves = []
    for chan in range(nchan):
      pen_color = self.DEFAULT_PEN_COLORS[chan % len(self.DEFAULT_PEN_COLORS)]
      self._curves.append(self.plot(self._time, self._data[chan].data(),
          pen=QtGraph.mkPen(pen_color, width=1), name=f'{chan}'))

    self.disableAutoRange()
    self.setXRange(self._time[0], self._time[-1]+self._sample_period, padding=0)
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
    if evt.text() == 'Y':
      self.enableAutoRange(axis=QtGraph.ViewBox.YAxis)
    elif evt.text() == 'y':
      self.zoomFitYRange()
    elif evt.text() == 'x':
      self.zoomFitXRange()
    elif evt.text() == 'a':
      self.zoomFitYRange()
      self.zoomFitXRange()
    else:
      pass

  def onMouseClicked(self, evt):
    if evt.double():
      self._snap_to_latest = True

  def zoomFitYRange(self):
    extents = np.array([self._data[i].extents() for i in range(self._nchan)])
    self.setYRange(np.min(extents), np.max(extents))

  def zoomFitXRange(self):
    self.setXRange(self._time[0], self._time[-1]+self._sample_period, padding=0)

  #Use the pyQt decorator here to reduce memory and improve performance
  @QtCore.pyqtSlot(list, name='onDataReady')
  def onDataReady(self, data):
    print(data)
    # Loop until the queue is empty
    for (chan, datum) in enumerate(data):
      self._data[chan].append(datum)
    self._time += self._sample_period

  #Use the pyQt decorator here to reduce memory and improve performance
  @QtCore.pyqtSlot(name='redraw')
  def redraw(self, jump_to_recent=False):
    # Update the plot
    prev_marker = self._last_redraw_time
    self._last_redraw_time = self._time[-1]
    [curr_xmin, curr_xmax] = self.viewRange()[0]
    if (curr_xmax >= prev_marker) or self._snap_to_latest:
      new_xmax = self._time[-1] + self._sample_period
      new_xmin = np.max([self._time[0], new_xmax - (curr_xmax - curr_xmin)])
      self.setXRange(new_xmin, new_xmax, padding=0)
      self._snap_to_latest = False
    for chan in range(self._nchan):
      self._curves[chan].setData(self._time, self._data[chan].data(), clipToView=True)
    self.sigRedraw.emit()