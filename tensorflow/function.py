#|___________________________________________________________________________|
#|# 见 w3cschool                                                             |
#|https://www.w3cschool.cn/tensorflow_python/tensorflow_python-w7yt2fwc.html |
#|___________________________________________________________________________|
import numpy as np
import tensorflow as tf

#张量:用张量这种数据结构来表示所有的数据.你可以把一个张量想象成一个n维的数组或列表.一个张量有一个静态类型和动态类型的维数.张量可以在图中的节点之间流通.

#Variable方法创建一个变量，当创建一个变量时，你将一个张量作为初始值传入构造函数Variable()
W = tf.Variable([.3], dtype=tf.float32)

#placeholder方法创建一个形参，由外部输入
x = tf.placeholder(tf.float32)


#Graph（图形）定义了计算。但它不计算任何东西，也不包含任何值，它只是定义您在代码中指定的操作。
#Session（会话）允许执行图形或部分图形。它为此分配资源（在一台或多台机器上）并保存中间结果和变量的实际值。
sess = tf.Session()

#run(self, fetches, feed_dict=None, options=None, run_metadata=None):
sess.run()

print([.3])