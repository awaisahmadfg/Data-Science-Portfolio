import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Dropout, Flatten
#from tensorflow.keras.layers import Conv2D, MaxPooling2D

from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model

def init():
    num_classes = 47
    img_size = 28
    img_rows, img_cols = 28, 28
    input_shape = (img_rows, img_cols, 1)
    model = tf.keras.Sequential()
    # model.add(keras.layers.Reshape((img_size,img_size,1), input_shape=(784,)))
    model.add(layers.Conv2D(filters=12, kernel_size=(5,5), strides=2, activation='relu', 
                                  input_shape=(img_size,img_size,1)))
    # model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(layers.Dropout(.5))
    
    model.add(layers.Conv2D(filters=18, kernel_size=(3,3) , strides=2, activation='relu'))
    # model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(layers.Dropout(.5))
    
    model.add(layers.Conv2D(filters=24, kernel_size=(2,2), activation='relu'))
    # model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
    
    # model.add(keras.layers.Conv2D(filters=30, kernel_size=(3,3), activation='relu'))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(units=150, activation='relu'))
    model.add(layers.Dense(units=num_classes, activation='softmax'))
    
    sess = tf.Session()
    graph = tf.get_default_graph()
    set_session(sess)

    #load woeights into new model
    model.load_weights("weights.h5")
    model._make_predict_function()
    print("Loaded Model from disk")

    #compile and evaluate loaded model
    model.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer=Adam(), metrics=['accuracy'])
    #loss,accuracy = model.evaluate(X_test,y_test)
    #print('loss:', loss)
    #print('accuracy:', accuracy)
    
    
    print(graph)
    return model, graph, sess