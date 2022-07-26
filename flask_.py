# -*- coding: utf-8 -*-
"""Flask_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j0CLQKHcF2Vvu23iwUjSusnY37PegG4O
"""

import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("fish.pkl","rb")
logistic_model = pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('fish.html')


@app.route('/predict',methods=["POST"])
def predict():
    """
    For rendering results on HTML GUI
    """
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = logistic_model.predict(final_features)
    #prediction = logistic_model.predict([[242.0,23.2,25.4,30.0,11.5200,4.0200]])
    return render_template('fish.html', prediction_text = 'The species that the fish belongs to {}'.format(str(prediction)))

if __name__=='__main__':
    app.run()

