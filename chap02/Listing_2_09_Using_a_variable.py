#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_9_Using_a_variable.py
#    Created:       <2019/04/13 16:27:49>
#    Last Modified: <2019/04/13 16:30:34>

import tensorflow as tf
sess = tf.InteractiveSession()

raw_data = [1., 2., 8., -1., 0., 5.5, 6., 13.]
spike = tf.Variable(False)
spike.initializer.run

for i in range(1, len(raw_data)):
    if raw_data[i] - raw_data[i - 1] > 5:
        updater = tf.assign(spike, True)
        updater.eval()
    else:
        tf.assign(spike, False).eval()
    print("Spike", spike.eval())

sess.close()
