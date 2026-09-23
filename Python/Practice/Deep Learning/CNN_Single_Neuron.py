# here we will connect the concepts of tensor flow with CNN

import tensorflow as tf

inputs = tf.constant([1.0,2.0,3.0])

weights = tf.constant([0.5,-0.2,0.8])

bias = tf.constant(0.1)

weighted_sum = tf.reduce_sum(inputs*weights) * bias

print("Inputs : ",inputs.numpy)     #1.0,2.0,3.0
print("Weights : ",weights.numpy)   #0.5,-0.2,0.8
print("bias : ",bias.numpy)         #0.1

print("Weighted Sum : ",weighted_sum)   #2.6

# wwe will send weighted sum to sigmoid- 
# coz sigmoid will be applied on the weighted sum

output = tf.sigmoid(weighted_sum)

print("Output : ",output.numpy())       #0.93