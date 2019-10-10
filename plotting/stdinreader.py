import select
import sys

from pyqtgraph.Qt import QtCore

def csv_to_float(line):
  return [float(s) for s in line.split(',')]

#Reads STDIN and converts text into numers
class StdinReader(QtCore.QObject):
  sigDataReady = QtCore.pyqtSignal(list)

  def __init__(self, converter=csv_to_float):
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
          data = self.conv(line)
          self.sigDataReady.emit(data)
      except ValueError:
        print(line)
