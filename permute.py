import random
import numpy as np

def shuffle_forward(l):
    order = range(len(l)); random.shuffle(order)
    return list(np.array(l)[order]), order

def shuffle_backward(l, order):
    l_out = [0] * len(l)
    for i, j in enumerate(order):
        l_out[j] = l[i]
    return l_out