#!/usr/bin/env python

import time

counter = 0
peak = 10.0
step = .1
burst = 5
delay = 0.001

while True:
  for _ in range(burst):
    print counter
    counter += step
    if ((counter >= peak) or (counter <= -peak)) :
      step = -step
  time.sleep(delay * burst)
