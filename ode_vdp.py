#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
使用`scipy.integrate.odeint`解`Van_Der_Pol`微分方程组
"""

import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt; plt.style.use("seaborn")

psi2 = lambda y, x : np.array([ y[1] , (1 - y[0]**2) * y[1] - y[0] ])

X, y0 = np.linspace(0, 20, num = 1024), [ 2 , 0 ]

y = integrate.odeint(psi2, y0, X)

plt.plot(X, y[ : , 0 ])
plt.plot(X, y[ : , 1 ])
plt.show()
