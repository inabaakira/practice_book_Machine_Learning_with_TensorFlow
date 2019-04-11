#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_7_Using_the_interactive_session_mode.py
#    Created:       <2019/04/11 18:32:01>
#    Last Modified: <2019/04/11 18:46:03>

import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.constant([[1., 2.]])
negMatrix = tf.negative(x)

result = negMatrix.eval()
print(result)

sess.close()
