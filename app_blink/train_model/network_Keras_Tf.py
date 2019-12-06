import tensorflow as tf
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import AveragePooling2D
from tensorflow.python.keras.layers import Activation, Flatten, Dense, Dropout
from tensorflow.python.keras.optimizers import RMSprop, Adam
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator, img_to_array
from tensorflow.python.keras.utils import to_categorical
from tensorflow.python.keras.models import load_model
from sklearn.model_selection import train_test_split
import numpy as np
from imutils import paths
import random
import cv2
import os
from tensorflow.python.keras.callbacks import Callback, ModelCheckpoint
from tensorflow.python.keras.callbacks import CSVLogger
from argparse import ArgumentParser
from lenet import LeNet

INIT_LR = 1e-3
BS = 124
n_class = 2 
EPOCHS = 1 # <<<
name_model = "tes" # <<< name anything
chanel = 1 # <<< color image
path_data =  r"D:\code_python\app_blink\train_model\npy\data_blinks_gray.npy"# <<< npy data
path_label = r"D:\code_python\app_blink\train_model\npy\label_blinks_gray.npy" # <<< npy label

model = LeNet.build_2(width=28, height=28, depth=chanel, classes=2) # <<< cnn weight
in_model = LeNet.build_2_inference(width=28, height=28, depth=chanel, classes=2) # <<< cnn inference


# check_point = ModelCheckpoint(r'model/{}.check'.format(name_model),
#                                 save_best_only=True,
#                                 monitor='val_loss',
#                                 verbose=1)

# csvSave = CSVLogger(f'{name_model}.csv')

Callback = [ModelCheckpoint(r'model/{}.check'.format(name_model),
                                save_best_only=True,
                                monitor='val_loss',
                                verbose=1), 
            CSVLogger(f'{name_model}.csv')]

data = np.load(path_data)
labels = np.load(path_label)

(trainX, testX, trainY, testY) = \
		train_test_split(data, labels, test_size=0.25, random_state=64)

trainY = to_categorical(trainY, num_classes=n_class)
testY = to_categorical(testY, num_classes=n_class)

aug = ImageDataGenerator(rotation_range=6, width_shift_range=0.1,
    	height_shift_range=0.1, shear_range=0.3, zoom_range=0.2,
    	horizontal_flip=True, fill_mode="nearest")

# model = lenet5(width=28, height=28, depth=1, classes=2)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt,metrics=["accuracy"])

H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
    	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
    	epochs=EPOCHS, verbose=1, callbacks=Callback)

model.save(f"{name_model}_weight.h5")

# in_model = lenet5_inference(width=28, height=28, depth=1, classes=2)
in_model.load_weights(f"{name_model}_weight.h5")

opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
in_model.compile(loss="binary_crossentropy", optimizer=opt,metrics=["accuracy"])

in_model.save(f"{name_model}_inference.h5")

load_model = load_model(f"{name_model}_inference.h5")

sess = K.get_session()
outname = "output_node"

tf.identity(load_model.outputs[0], name=outname)
constant_graph = tf.graph_util.convert_variables_to_constants(sess, 
							sess.graph.as_graph_def(), [outname])
tf.io.write_graph(constant_graph, r"model", f"{name_model}_TF.pb", as_text=False)
 
