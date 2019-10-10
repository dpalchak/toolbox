#!/usr/bin/env python3

import time
import functools

counter = 0
peak = 10.0
step = .1
burst = 5
delay = 0.001

print = functools.partial(print, flush=True)

while True:
  for _ in range(burst):
    print(f"{counter}, {round(counter+50,1)}")
    counter += step
    counter = round(counter, 1)
    if ((counter >= peak) or (counter <= -peak)) :
      step = -step
  time.sleep(delay * burst)
