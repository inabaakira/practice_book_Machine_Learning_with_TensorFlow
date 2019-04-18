#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: regression.py
#    Created:       <2019/04/18 13:39:50>
#    Last Modified: <2019/04/18 13:42:28>

import numpy as np
import matplotlib.pyplot as plt

x_train = np.linspace(-1, 1, 101)
y_train = 2 * x_train + np.random.randn(*x_train.shape) * 0.33

plt.scatter(x_train, y_train)
plt.show()
