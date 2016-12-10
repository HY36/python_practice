# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import anderson
from scipy.stats import normaltest


def binomial():
    '''二项分布'''
    cash = np.zeros(10000)
    cash[0] = 1000
    outcome = np.random.binomial(9, 0.5, size=len(cash))

    for i in range(1, len(cash)):
        if outcome[i] < 5:
            cash[i] = cash[i-1] - 1
        elif outcome[i] < 10:
            cash[i] = cash[i - 1] + 1
        else:
            raise AssertionError("Unexpected outcome " + outcome[i])

    print(outcome.min(), outcome.max())

    plt.plot(np.arange(len(cash)), cash)
    plt.show()


def normal():
    N = 1000
    normal_value = np.random.normal(size=N)
    dummy, bins, dummy = plt.hist(normal_value, int(np.sqrt(N)), normed=True, lw=1)
    sigma = 1
    mu = 0
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu) ** 2 / (2 * sigma ** 2)), lw=2)
    plt.show()


def normal_test():
    flutrends = np.loadtxt("goog_flutrends.csv", delimiter=',', usecols=(1, ), skiprows=1,
                           converters={1: lambda s: float(s or 0)},unpack=True)
    N = len(flutrends)
    normal_values = np.random.normal(size=N)
    zero_values = np.zeros(N)

    # print shapiro(normal_values)
    # print shapiro(zero_values)
    # print shapiro(flutrends)

    # print anderson(normal_values)
    # print anderson(zero_values)
    # print anderson(flutrends)

    print normaltest(normal_values)
    print normaltest(zero_values)
    print normaltest(flutrends)

if __name__ == '__main__':
    binomial()
