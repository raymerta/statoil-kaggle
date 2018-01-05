import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from os.path import join as opj
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
#matplotlib inline

#Import Keras.
from matplotlib import pyplot
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Input, Flatten, Activation
from keras.layers import GlobalMaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers import Concatenate, Dense, LSTM, Input, concatenate
from keras.models import Model
from keras import initializers
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping




#Load the data.
train = pd.read_json("static/json/train.json")
train['inc_angle'] = train['inc_angle'].replace('na', 0.).astype(np.float32)

test = pd.read_json("static/json/test.json")
test['inc_angle'] = test['inc_angle'].replace('na', 0.).astype(np.float32)

#Generate the training data
#Create 3 bands having HH, HV and avg of both
def makeAugmentedCopies(images):
    c1 = images
    c2 = np.array([np.rot90(image) for image in c1])
    c3 = np.array([np.rot90(image) for image in c2])
    c4 = np.array([np.rot90(image) for image in c3])
    cf1 = np.array([np.fliplr(image) for image in c1])
    cf2 = np.array([np.rot90(image) for image in cf1])
    cf3 = np.array([np.rot90(image) for image in cf2])
    cf4 = np.array([np.rot90(image) for image in cf3])
    return np.concatenate((c1, c2, c3, c4, cf1, cf2, cf3, cf4), axis=0)


X_band_1=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in train["band_1"]])
X_band_1=makeAugmentedCopies(X_band_1)
X_band_2=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in train["band_2"]])
X_band_2=makeAugmentedCopies(X_band_2)
X_train = np.concatenate([X_band_1[:, :, :, np.newaxis], X_band_2[:, :, :, np.newaxis],((X_band_1+X_band_2)/2)[:, :, :, np.newaxis]], axis=-1)

ang = train['inc_angle']
angles_train=np.concatenate((ang,ang,ang,ang,ang,ang,ang,ang), axis=0)


def getModel():
    p_activation = "relu"
    #
    image_input = Input(shape=(75, 75, 3))
    other_input = Input(shape=(1,))
    #Building the model
    model=Sequential()
    #
    #
    #Conv Layer 1
    gmodel = Conv2D(16, kernel_size = (3,3), activation=p_activation, input_shape=(75, 75, 3))(image_input)
    gmodel = Dropout(0.2)(gmodel)
    gmodel = BatchNormalization()(gmodel)
    #Conv Layer 2
    gmodel = Conv2D(32, kernel_size = (3,3), activation=p_activation)(gmodel)
    gmodel = Dropout(0.2)(gmodel)
    gmodel = BatchNormalization()(gmodel)
    gmodel = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(gmodel)
    #Conv Layer 3
    gmodel = Conv2D(64, kernel_size = (3,3), activation=p_activation)(gmodel)
    gmodel = Dropout(0.2)(gmodel)
    gmodel = BatchNormalization()(gmodel)
    #Conv Layer 4
    gmodel = Conv2D(128, kernel_size = (3,3), activation=p_activation)(gmodel)
    gmodel = Dropout(0.2)(gmodel)
    gmodel = BatchNormalization()(gmodel)
    gmodel = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(gmodel)
    output1 = Flatten()(gmodel)
    #
    #
    #
    #
    #
    #
    model = concatenate([output1, other_input])
    #
    model = Dense(256, activation=p_activation)(model)
    model = Dropout(0.2)(model)
    model = BatchNormalization()(model)
    #
    model = Dense(64, activation=p_activation)(model)
    model = Dropout(0.2)(model)
    model = BatchNormalization()(model)
    #
    predicts = Dense(1, activation="sigmoid")(model)
    #
    model = Model(inputs=[image_input, other_input], outputs=predicts)
    model.compile(loss="binary_crossentropy",
        optimizer=Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0),
        metrics=["accuracy"])
    model.summary()
    return model


def get_callbacks(filepath, patience=2):
    es = EarlyStopping('val_loss', patience=patience, mode="min")
    msave = ModelCheckpoint(filepath, save_best_only=True)
    return [es, msave]


file_path = ".model_weights_inc_angle.hdf5"
callbacks = get_callbacks(filepath=file_path, patience=100)

tr=train['is_iceberg']
target_train=np.concatenate((tr,tr,tr,tr,tr,tr,tr,tr), axis=0)
X_train_cv, X_valid, y_train_cv, y_valid, ang_tr, ang_val = train_test_split(X_train, target_train, angles_train, random_state=1, train_size=0.75)

#Without denoising, core features.
import os
gmodel=getModel()
gmodel.fit([X_train_cv, ang_tr], y_train_cv,
          batch_size=24,
          epochs=250,
          verbose=1,
          validation_data=([X_valid, ang_val], y_valid),
          callbacks=callbacks)

gmodel.load_weights(filepath=file_path)
score = gmodel.evaluate(X_valid, y_valid, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

X_band_test_1=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in test["band_1"]])
X_band_test_2=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in test["band_2"]])
X_test = np.concatenate([X_band_test_1[:, :, :, np.newaxis]
                          , X_band_test_2[:, :, :, np.newaxis]
                         , ((X_band_test_1+X_band_test_2)/2)[:, :, :, np.newaxis]], axis=-1)
predicted_test=gmodel.predict_proba(X_test)

submission = pd.DataFrame()
submission['id']=test['id']
submission['is_iceberg']=predicted_test.reshape((predicted_test.shape[0]))

from time import gmtime, strftime
submission.to_csv('submission_' + strftime("%d_%H_%M_%S", gmtime()) + '.csv', index=False)
