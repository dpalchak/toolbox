import select
import sys

from pyqtgraph.Qt import QtCore

#Reads STDIN and converts text into numers
class StdinReader(QtCore.QObject):
  sigDataReady = QtCore.pyqtSignal(float)

  def __init__(self, converter=float):
    super(StdinReader, self).__init__()
    self.conv = converter
    self.running = False
    self.thread = QtCore.QThread()
    self.moveToThread(self.thread)
    self.thread.started.connect(self.run)

  def start(self):
    self.thread.start()

  def stop(self):
    self.running = False
    self.thread.quit()
    self.thread.wait()

  def run(self):
    self.running = True
    while self.running:
      i, o, e = select.select([sys.stdin], [], [], 0.1)
      if not i:
        continue
      line = sys.stdin.readline().rstrip()
      try:
        if line:
          n = self.conv(line)
          self.sigDataReady.emit(n)
      except ValueError:
        print(line)
