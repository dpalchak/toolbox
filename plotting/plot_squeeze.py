#!/usr/bin/env python3

import argparse
import sys

from liveplotwidget import LivePlotWidget
from pyqtgraph.Qt import QtGui
from serialreader import SerialReader

def get_strains(line):
  msg = line.split(b',')[1]
  strains = msg.split()[2:8]
  return [float(s) for s in strains]

def main():
  parser = argparse.ArgumentParser(description='Real-time serial port plot')
  parser.add_argument('-b', '--baud', type=int, default='112500', help='Set the baud rate')
  parser.add_argument('-d', '--device', type=str, default='/dev/ttyUSB0',
                      help='The path and filename of the device to open.')
  args = parser.parse_args()

  app = QtGui.QApplication(sys.argv)

  reader = SerialReader(args.device, args.baud, converter=get_strains)
  plot = LivePlotWidget(sample_freq=50, buffer_secs=600.0, nchan=6)
  reader.sigDataReady.connect(plot.onDataReady)

  plot.setWindowTitle(args.device)
  plot.show()
  reader.start()
  ret = app.exec_()
  reader.stop()
  sys.exit(ret)

if __name__ == '__main__':
  main()
