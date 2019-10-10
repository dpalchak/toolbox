
import serial
from pyqtgraph.Qt import QtCore

# Reads the serial input stream and converts text into numbers
class SerialReader(QtCore.QObject):
  sigDataReady = QtCore.pyqtSignal(list)

  def __init__(self, device, baud, converter=float, timeout=0.001, **kwargs):
    super(SerialReader, self).__init__()
    self.serial = serial.Serial(device, baud, timeout=timeout, **kwargs)
    self.conv = converter
    self.fragment = bytearray()
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
    self.serial.close()

  def run(self):
    self.running = True
    while self.running:
      input = self.serial.read(4096)
      if len(input) > 0:
        buf = self.fragment + input
        lines = buf.split(b'\n')
        self.fragment = lines.pop()
        for line in lines:
          try:
            data = self.conv(line)
            if data is not None:
              self.sigDataReady.emit(data)
          except (ValueError, IndexError):
            print(line)
