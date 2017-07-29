import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import csv
from Test import Test

data_file = open('data.csv', newline='')
reader = csv.reader(data_file)
header = next(reader)

test1 = Test(next(reader))
print("p1 =",test1.p1)
print("p2 =",test1.p2)
print("v1 =",test1.v1)
print("v2 =",test1.v2)
print("tcpa =",test1.find_tcpa())

t = np.arange(0, 3, 0.02)
d = np.vectorize(test1.dist)(t)


lines = plt.plot(t, d)
plt.setp(lines[0], linewidth=4)
plt.savefig("test.png")



