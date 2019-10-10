#!/usr/bin/env python

import sys

from liveplotwidget import LivePlotWidget
from stdinreader import StdinReader
from pyqtgraph.Qt import QtGui


def main():
  app = QtGui.QApplication(sys.argv)

  reader = StdinReader()

  plot = LivePlotWidget(tstep=0.001, history=50)
  reader.sigDataReady.connect(plot.onDataReady)

  plot.setWindowTitle('STDIN plot')
  plot.show()
  reader.start()
  ret = app.exec_()
  reader.stop()
  sys.exit(ret)

if __name__ == '__main__':
  main()
