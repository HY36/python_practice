import numpy as np
import matplotlib.pyplot as plt

salary = np.loadtxt('MLB2008.csv', delimiter=',', usecols=(1, ),
                    skiprows=1, unpack=True)

triples = np.arange(0, len(salary), 3)
signs = np.ones(len(salary))
signs[triples] = -1
ma_log = np.ma.log(salary * signs)

dev = salary.std()
avg = salary.mean()
inside = np.ma.masked_outside(salary, avg - dev, avg + dev)

plt.subplot(311)
plt.plot(salary)

plt.subplot(312)
plt.plot(np.exp(ma_log))

plt.subplot(313)
plt.plot(inside)

plt.show()