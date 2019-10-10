#!/usr/bin/env python

import argparse
import sys
import re

from liveplotwidget import LivePlotWidget
from serialreader import SerialReader
from pyqtgraph.Qt import QtGui

line_number_re = re.compile(r'^.*?\.cc\s+(\d+)\s|')
def get_line_number(log_msg):
  m = line_number_re.match(log_msg)
  if m is not None:
    line_num = float(m.groups()[0])
    print("(%f) %s" % (line_num, log_msg))
    return line_num
  else:
    raise ValueError(log_msg)

def main():
  parser = argparse.ArgumentParser(description='Real-time serial port plot')
  parser.add_argument('-b', '--baud', type=int, default='250000', help='Set the baud rate')
  parser.add_argument('-d', '--device', type=str, default='/dev/ttyUSB0',
                      help='The path and filename of the device to open.')
  args = parser.parse_args()

  app = QtGui.QApplication(sys.argv)

  reader = SerialReader(args.device, args.baud, converter=get_line_number)
  plot = LivePlotWidget(tstep=(1.0/240), history=60)
  reader.sigDataReady.connect(plot.onDataReady)

  plot.setWindowTitle(args.device)
  plot.show()
  reader.start()
  ret = app.exec_()
  reader.stop()
  sys.exit(ret)

if __name__ == '__main__':
  main()
