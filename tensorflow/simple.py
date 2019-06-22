# 简单的线性回归例子
import tensorflow as tf

# 创建变量，tens
a = tf.Variable([0.3], dtype=tf.float32)
b = tf.Variable([-0.3], dtype=tf.float32)
# 创建占位符
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
# 定义预测函数
linear_model = a * x + b
# loss 最普通的的均方差
loss = tf.reduce_sum(tf.square(linear_model - y))  # sum of the squares

# 定义一个优化器，Gradient梯度 Descent下降 Optimizer优化器
optimizer = tf.train.GradientDescentOptimizer(0.01)
# 优化器最小化loss
train = optimizer.minimize(loss)

# training data 这个数据自己改动
x_train = [1, 2, 3, 4]
y_train = [0, 1, 2, 3]

# training loop
# 这个 init的值如下：
#  name: "init"
# op: "NoOp"
# input: "^Variable/Assign"
# input: "^Variable_1/Assign"
# 注意：只要用到变量，就一定要run一下initialize_all_variables() (global_variables_initializer)来初始化变量。
sess = tf.Session()
sess.run(tf.global_variables_initializer())  # reset values to wrong

# 迭代一千次后，参数已经训练好
for i in range(1000):
    temp = sess.run(train, {x: x_train, y: y_train})

# 送入训练好的参数，求出loss
# evaluate training accuracy
curr_a, curr_b, curr_loss = sess.run([a, b, loss], {x: x_train, y: y_train})
print("a: %s b: %s loss: %s" % (curr_a, curr_b, curr_loss))
