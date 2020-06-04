# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:05:40 2020

@author: gaurav sahani
"""


from flask import Flask, render_template, request
from sklearn.externals import joblib
import numpy as np

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            SepalLengthCm = float(request.form['SepalLengthCm'])
            SepalWidthCm = float(request.form['SepalWidthCm'])
            PetalLengthCm = float(request.form['PetalLengthCm'])
            PetalWidthCm = float(request.form['PetalWidthCm'])
            pred_args = [ SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            iris_cls = open("classification_model.pkl", "rb")
            ml_model = joblib.load(iris_cls)
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)
        
        except ValueError:
            return "Please Check if values are written correctly"
    return render_template('predict.html', prediction=model_prediction)

if __name__ == "__main__":
    app.run()