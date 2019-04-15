#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_11_Loading_variables.py
#    Created:       <2019/04/15 12:02:30>
#    Last Modified: <2019/04/15 12:07:53>

import tensorflow as tf
sess = tf.InteractiveSession()

spikes = tf.Variable([False] * 8, name='spikes')
# spikes.initializer.run()
saver = tf.train.Saver()

saver.restore(sess, "./spikes.ckpt")
print(spikes.eval())

sess.close()
