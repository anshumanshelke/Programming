import tensorflow as tf

tensor1 = tf.constant([10,20,30])
tensor2 = tf.constant([1,2,3])

addition = tf.add(tensor1,tensor2)
print("Addition is : ",addition)    #11,22, 33

substraction = tf.subtract(tensor1,tensor2)
print("substraction is : ",substraction)    #9,18,27

multiplication = tf.multiply(tensor1,tensor2)
print("multiplication is : ",multiplication)    #10,40,90

division = tf.divide(tensor1,tensor2)
print("division is : ",division)    #10.0,10.0,10.0

square = tf.square(tensor1)
print("Square : ",square)   #100,400,900

sum = tf.reduce_sum(tensor1)    #60 .... coz 10+20+30
print("Reduced sum : ",sum)

mean = tf.reduce_mean(tensor1)  # 20 .... coz ->  (10+20+30) / 3
print("Mean is : ",mean)