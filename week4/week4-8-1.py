import tensorflow as tf
import numpy as np


'''
x = np.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 114.76, 59.3, 116.03])
y = np.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
'''

x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])


xa = tf.reduce_mean(x)
ya = tf.reduce_mean(y)

Numerator = tf.constant(0.)
Denominator = tf.constant(0.)

for i in range(len(x)):  

    Numerator += (x[i] - xa) * (y[i] - ya)
    Denominator += tf.pow((x[i] - xa), 2)

w = Numerator/Denominator
b = ya - w * xa

print("w: {}".format(w))
print("b: {}".format(b))

