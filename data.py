import numpy as np
import matplotlib.pyplot as plt

N = 1000


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
    normal_value = np.random.normal(size=N)
    dummy, bins, dummy = plt.hist(normal_value, np.sqrt(N), normed=True, lw=1)
    sigma = 1
    mu = 0
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu) ** 2 / (2 * sigma ** 2)), lw=2)
    plt.show()

if __name__ == '__main__':
    normal()