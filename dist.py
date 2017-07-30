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
print(test1.find_tcpa())
test1.make_test()
