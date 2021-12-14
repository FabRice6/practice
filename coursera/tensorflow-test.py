'''
Just the basics to test if tensorflow still works on my macbook M1 chip:
1) Find minimum of function J(w) = wˆ2 - 10*w + 25


UPDATE: Still having errors:
NotFoundError: dlopen(/Users/fabriceverhaert/miniforge3/envs/ai-ml/lib/python3.8/site-packages/tensorflow-plugins/libmetal_plugin.dylib, 6): Symbol not found: _OBJC_CLASS_$_MPSGraphCompilationDescriptor
  Referenced from: /Users/fabriceverhaert/miniforge3/envs/ai-ml/lib/python3.8/site-packages/tensorflow-plugins/libmetal_plugin.dylib (which was built for Mac OS X 12.0)
  Expected in: /System/Library/Frameworks/MetalPerformanceShadersGraph.framework/Versions/A/MetalPerformanceShadersGraph
'''
import numpy as np
import tensorflow as tf

w = tf.Variable(0, dtype=tf.float32)
cost = tf.add(tf.add(w**2, tf.multiply(-10, w)), 25)
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost) # learning rate 0.01

# The next lines are quite idiomatic, standard stuff
init = tf.global_variables_initializer()
session = tf.Session() # start the session
session.run(init) # run session with initial global variables
print(session.run(w))
