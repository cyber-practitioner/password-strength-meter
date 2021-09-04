
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib as mt
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score
import sklearn.metrics as skm
import math
import joblib,weakref
import keras

data=pd.read_csv(r"C:\Users\FIREBLZE\Desktop\Python Codes and Datasets\NLP DATASET.csv",encoding='utf-8',error_bad_lines=False)
data.dropna(inplace=True)
password_tuple=np.array(data)
import random
random.shuffle(password_tuple)
x=[labels[0] for labels in password_tuple]
y=[labels[1] for labels in password_tuple]
def word_divide_char(inputs):
    character=[]
    for i in inputs:
        character.append(i)
    return character

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(tokenizer=word_divide_char)

X=vectorizer.fit_transform(x)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.25)
import tensorflow as tf
ann=tf.keras.models.Sequential()
X_train_ann=X_train.toarray()

ann.add(tf.keras.layers.Dense(units=300,activation='relu'))
ann.add(tf.keras.layers.Dense(units=300,activation='relu'))
ann.add(tf.keras.layers.Dense(units=3,activation=tf.keras.activations.softmax))
ann.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics =['accuracy'])
history=ann.fit(X_train_ann,np.array(y_train), batch_size=37,verbose=1,epochs=16)
dt=np.array(['a21r312d'])
pred=vectorizer.transform(dt)
sample=ann.predict(pred.toarray())
prediction=print(np.argmax(sample))

ann.save('ANN.h5')