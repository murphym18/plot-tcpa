import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

px10 = 0
py10 = 0
pz10 = 0

vx1 = 1
vy1 = 0
vz1 = 0

px20 = 5
py20 = 0
pz20 = 0

vx2 = -1
vy2 = 1
vz2 = 0

def x1(t):
  return px10 + vx1 * t
def y1(t):
  return py10 + vy1 * t
def z1(t):
  return pz10 + vz1 * t
def x2(t):
  return px20 + vx2 * t
def y2(t):
  return py20 + vy2 * t
def z2(t):
  return pz20 + vz2 * t

def dist2(t):
  dx = x1(t) - x2(t)
  dy = y1(t) - y2(t)
  dz = z1(t) - z2(t)
  return dx*dx + dy*dy + dz*dz

def dist(t):
  return np.sqrt(dist2(t))


t = np.arange(0, 5, 0.02)
d = np.vectorize(lambda t: dist(t))(t)

lines = plt.plot(t, d)
plt.setp(lines[0], linewidth=4)
#plt.show()
plt.savefig("test.png")
