#!/usr/bin/env python

import argparse
import sys
import re

from liveplotwidget import LivePlotWidget
from serialreader import SerialReader
from pyqtgraph.Qt import QtGui

eda_re = re.compile(r'^EDA\ 0x([A-F0-9]{4})')
def parse_eda(log_msg):
  m = eda_re.match(log_msg)
  if m is not None:
    sample = int(str(m.groups()[0]), 16)
    print("(%d) %s" % (sample, log_msg))
    return sample
  else:
    raise ValueError(log_msg)

def main():
  parser = argparse.ArgumentParser(description='Real-time serial port plot')
  parser.add_argument('-b', '--baud', type=int, default='250000', help='Set the baud rate')
  parser.add_argument('-d', '--device', type=str, default='/dev/ttyUSB0',
                      help='The path and filename of the device to open.')
  args = parser.parse_args()

  app = QtGui.QApplication(sys.argv)

  reader = SerialReader(args.device, args.baud, converter=parse_eda)
  plot = LivePlotWidget(tstep=1.0, history=1000)
  reader.sigDataReady.connect(plot.onDataReady)

  plot.setWindowTitle(args.device)
  plot.show()
  reader.start()
  ret = app.exec_()
  reader.stop()
  sys.exit(ret)

if __name__ == '__main__':
  main()
