import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import csv
from Test import Test

data_file = open('data.csv', newline='')
reader = csv.reader(data_file)
header = next(reader)
print(header)
test1 = Test(next(reader))
p1 = [0.0, 0.0, 0.0]
v1 = [1.0, 0.0, 0.0]

p2 = [5.0, 0.0, 0.0]
v2 = [-1.0, 1.0, 0.0]

def make_funcs(p, v):
    def make_func(i):
        return lambda t: p[i] + t*v[i]
    return (make_func(0), make_func(1), make_func(2))

x1, y1, z1 = make_funcs(p1, v1)
x2, y2, z2 = make_funcs(p2, v2)

def dist2(t):
  dx = x1(t) - x2(t)
  dy = y1(t) - y2(t)
  dz = z1(t) - z2(t)
  return dx*dx + dy*dy + dz*dz

def dist(t):
  return np.sqrt(dist2(t))

def make_test(name, dist_func, tcpa, p1, v1, p2, v2):
    make_test_docs()
    make_test_code()

t = np.arange(0, 5, 0.02)
d = np.vectorize(lambda t: dist(t))(t)

lines = plt.plot(t, d)
plt.setp(lines[0], linewidth=4)
plt.savefig("test.png")
