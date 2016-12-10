# -*- coding: utf-8 -*-

import numpy
from scipy import misc
import matplotlib.pyplot as plt


def mask_demo():
    ascent = misc.ascent()
    random_mask = numpy.random.randint(0, 2, size=ascent.shape)
    plt.subplot(221)
    plt.title("ascent")
    plt.imshow(ascent)
    plt.axis('off')

    masked_array = numpy.ma.array(ascent, mask=random_mask)
    print masked_array

    plt.subplot(222)
    plt.title("masked")
    plt.imshow(masked_array)
    plt.axis('off')

    plt.subplot(223)
    plt.title("Log")
    plt.imshow(numpy.log(ascent))
    plt.axis('off')

    plt.subplot(224)
    plt.title("Log Masked")
    plt.imshow(numpy.log(masked_array))
    plt.axis('off')

    plt.show()

if __name__ == '__main__':
    mask_demo()