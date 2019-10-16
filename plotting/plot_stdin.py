#!/usr/bin/env python3

import sys

from liveplotwidget import LivePlotWidget
from stdinreader import StdinReader
from pyqtgraph.Qt import QtGui


def main():
  app = QtGui.QApplication(sys.argv)

  reader = StdinReader()

  plot = LivePlotWidget(sample_freq=1000, buffer_secs=60.0, nchan=2)
  reader.sigDataReady.connect(plot.onDataReady)

  plot.setWindowTitle('STDIN plot')
  plot.show()
  reader.start()
  ret = app.exec_()
  reader.stop()
  sys.exit(ret)

if __name__ == '__main__':
  main()
