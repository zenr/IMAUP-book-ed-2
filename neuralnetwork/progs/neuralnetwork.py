import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.datasets import mnist

# Fetch the train and test data.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the image so that all pixel values
# are between -0.5 and +0.5.
x_train = (x_train / 255) - 0.5
x_test = (x_test / 255) - 0.5

# Reshape the train and test images to size 784 long vector.
x_train = x_train.reshape((-1, 784))
x_test = x_test.reshape((-1, 784))

# Define the neural network model with 2 hidden layer
# of size 64 nodes each.
model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax'),
])

# Compile the model using Adam optimizer and use
# the cross entropy loss.
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model.
model.fit(x_train, to_categorical(y_train), epochs=5,
          batch_size=32)
