import numpy as np
import matplotlib.pyplot as plt

def f(N, r = 0.1, r1 = 0, r2 = 0):
    dN_dt = -r*N
    return dN_dt

def RK2(N0,  h = 0.01, t = 0, main_label='Radioactive Decay(RK2 method)', x_label="Time", y_label="N(t)"):
    tlist, Nlist = [], []
    for i in range(5000):
        k1 = h * f(N0)
        k2 = h * f(N0 + k1)
        t += h
        N0 += (k1 + k2)/2
        tlist.append(t)
        Nlist.append(N0)
    
    plt.plot(tlist, Nlist, label= main_label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend()
    plt.show()
