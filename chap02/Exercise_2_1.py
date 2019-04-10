#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Exercise_2_1.py
#    Created:       <2019/04/10 15:30:14>
#    Last Modified: <2019/04/10 15:57:43>

import tensorflow as tf

m = tf.ones([500, 500]) * 0.5
print(m)
with tf.Session() as sess:
    print("m[0][0] = {}, m[499][499] = {}".format(m[0][0].eval(), m[499][499].eval()))
