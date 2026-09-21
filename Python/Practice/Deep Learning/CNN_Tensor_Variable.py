import tensorflow as tf

weight = tf.Variable(5.0)

print("Initial weight value : ",weight)     #5.0

#   OR- use this--

#print("Initial weight value : ",weight.numpy())

weight.assign(10.0)
print("Update weight : ",weight.numpy())    #10.0

weight.assign_add(2.5)
print("Update weight : ",weight.numpy())    #12.5

weight.assign_sub[1.5]
print("Update weight : ",weight.numpy())    #11.0
