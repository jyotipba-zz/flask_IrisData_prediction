from flask import Flask, render_template, flash, url_for, request
from forms import featureForm
import pickle
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = "flask machine learning model"

@app.route("/", methods = ['GET', 'POST'])
def home():
    form = featureForm()
    if form.validate_on_submit():
        sepal_length= form.sepal_length.data
        sepal_width = form.sepal_width.data
        petal_length = form.petal_length.data
        petal_width = form.petal_width.data
        with open ("./static/final_svm_model.pkl",'rb') as pickle_file:
              model = pickle.load(pickle_file)

        data = np.array([sepal_length,sepal_width, petal_length, petal_width]).reshape(1,-1)
        prediction= model.predict(data)
        predict_result = ""

        if prediction == 0:
            predict_result = 'setosa'
        elif prediction == 1:
            predict_result =  'versicolor'
        else :
            predict_result = 'virginica'

        return render_template("home.html", form=form, result = predict_result)
    return render_template("home.html", form = form)
