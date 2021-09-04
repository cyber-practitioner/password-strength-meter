from django.shortcuts import render
#from . import  keras_model
# from  keras_model import vectorizer
import numpy as np,pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
#from tensorflow.keras.models import load_model
import sklearn
#from keras_model import vectorizer,ann
#from tensorflow.keras.models import load_model
# Create your views here.
def home(request):
    return render(request,'meter/home.html')

def result(request):

    data=pd.read_csv(r"C:\Users\FIREBLZE\Desktop\Python Codes and Datasets\NLP DATASET.csv",encoding='utf-8',error_bad_lines=False)
    data.dropna(inplace=True)
    password_tuple=np.array(data)
    import random
    random.shuffle(password_tuple)
    x=[labels[0] for labels in password_tuple]
    y=[labels[1] for labels in password_tuple]

  #  context={}
    def word_divide_char(inputs):
        character = [ ]
        for i in inputs:
            character.append(i)
        return character
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
    history=ann.fit(X_train_ann,np.array(y_train), batch_size=37,verbose=1,epochs=12)

    dt=request.POST.get('password')
    
    #print(dt)
   # context['password']=
    d=np.array([dt])
    pred=vectorizer.transform(d)
    #print(pred.toarray())
    #new_ann=load_model('ANN.h5')
    sample=ann.predict(pred.toarray()) #error here
   #print(sample)
    prediction=np.argmax(sample)
    print(prediction)
  
    return render(request,'meter/result.html',{'pred':prediction})