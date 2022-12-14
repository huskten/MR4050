import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os
from modellib import splitSequence, createTrainData

Ncheckpoint = "Ncheckpoints/Ncheckpoint"
checkpoint_dir = os.path.dirname(Ncheckpoint)


# Create a callback that saves the model's weights
Callback = tf.keras.callbacks.ModelCheckpoint(filepath=Ncheckpoint,
                                                 save_weights_only=True,
                                                 verbose=1)


########################################################################

Data = []

# createTrainData(Data, 'gimpedpinatracemedium.out')
createTrainData(Data, 'traceheavy.out')

n_steps = 5

A, b = splitSequence(Data, n_steps = 5)

# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
A = A.reshape((A.shape[0], A.shape[1], n_features))

Model = tf.keras.Sequential()
Model.add(layers.LSTM(256, activation='relu', input_shape=(n_steps, n_features)))
Model.add(layers.Dense(1))

Model.layers

#Model.summary()

Model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.MeanSquaredError())

Model.fit(A, b, epochs=200, verbose=1)

PredictSect = []

# Model.save('savedModels/normModel')
Model.save('savedModels/normModel2')