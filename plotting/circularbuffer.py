
import numpy as np

class CircularBuffer:
  def __init__(self, capacity, dtype=np.float, init_value=None):
    if init_value is None:
      init_value = dtype(0)
    self._capacity = capacity
    self._data = np.zeros(capacity, dtype=dtype) + init_value
    self._extents = np.array([np.min(self._data), np.max(self._data)])

  def append(self, data):
    # Force data to single dimension array
    data = np.ravel(data)
    count = len(data)
    self._data = np.roll(self._data, -count)
    self._data[-count:] = data
    self._extents[0] = np.min([self._extents[0], np.min(data)])
    self._extents[1] = np.max([self._extents[1], np.max(data)])

  def data(self):
    return self._data

  def extents(self):
    return self._extents

  def __len__(self):
    return self._capacity

