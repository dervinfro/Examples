#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:02:58 2021

@author: user

https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
"""

import tensorflow as tf
print(tf.__version__)

a = tf.constant(5)
b = tf.constant(2)
c = tf.constant(3)

d = tf.multiply(a,b)
e = tf.add(c,d)
f = tf.subtract(d,e)

print(f)