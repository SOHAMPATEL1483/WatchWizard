import tensorflow as tf
from tensorflow import keras
# from .models import Profile
import json
import numpy as np
import pickle


# def cofi_cost_func_v(X, W, b, Y, R, lambda_):

#     j = (tf.linalg.matmul(X, tf.transpose(W)) + b - Y)*R
#     J = 0.5 * tf.reduce_sum(j**2) + (lambda_/2) * \
#         (tf.reduce_sum(X**2) + tf.reduce_sum(W**2))
#     return J


# def train_model(user):
#     print("sucsessfully called train_model")
#     userprofile = Profile.objects.get(user=user)
#     w = json.loads(userprofile.W)
#     b = json.loads(userprofile.B)
#     y = json.loads(userprofile.Y)
#     r = json.loads(userprofile.R)
#     train_w = tf.convert_to_tensor(value=w)
#     train_b = tf.convert_to_tensor(value=b)
#     train_w = tf.reshape(train_w, [1, 100])
#     train_b = tf.reshape(train_b, [1, 1])
#     train_w = tf.cast(train_w, tf.float64)
#     train_b = tf.cast(train_b, tf.float64)
#     train_w = tf.Variable(train_w, name="train_w")
#     train_b = tf.Variable(train_b, name="train_b")
#     train_r = []
#     train_r.append(0)

#     for i in range(1, 974):
#         if i not in r:
#             train_r.append(0)
#         else:
#             train_r.append(1)

#     y = np.array(y)
#     train_r = np.array(train_r)
#     X = pickle.load(open('./static/X.pkl', 'rb'))
#     Ymean = pickle.load(open('./static/Ymean.pkl', 'rb'))
#     ynorm = y - np.multiply(Ymean, train_r)
#     optimizer = keras.optimizers.Adam(learning_rate=1e-1)

#     print(train_w.dtype)
#     print(train_b.dtype)
#     print(X.dtype)
#     print(type(train_r))
#     print("sucsessfully get all the parameter")
#     iterations = 100
#     lambda_ = 1
#     for iter in range(iterations):

#         with tf.GradientTape() as tape:

#             cost_value = cofi_cost_func_v(
#                 X, train_w, train_b, ynorm, train_r, lambda_)

#         grads = tape.gradient(cost_value, [train_w, train_b])

#         optimizer.apply_gradients(zip(grads,  [train_w, train_b]))

#         if iter % 10 == 0:
#             print(f"Training loss at iteration {iter}: {cost_value:0.1f}")

#     w = train_w.numpy().tolist()
#     b = train_b.numpy().tolist()
#     print("Succesfully trained")
#     print(type(w))
#     print(type(b))
#     userprofile.W = str(w)
#     userprofile.B = str(b)

#     try:
#         userprofile.full_clean()
#         userprofile.save()
#     except:
#         print("Validation error")


mat = pickle.load(open(
    'C:/Users/snehp/Desktop/Project/Movie Recommandation/movie-system-backend-master/static/similarity.pkl', 'rb'))
print(type(mat))
print(mat.shape)
