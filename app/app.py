from flask import (Flask, render_template, flash, url_for, request,
      jsonify,send_file,send_from_directory, redirect)
from forms import FeatureForm, FileForm
import pickle
import numpy as np
import pandas as pd
from werkzeug.utils import secure_filename
from bing_image_search import search_image
import uuid


app = Flask(__name__)
app.config['SECRET_KEY'] = "flask machine learning model"

@app.route("/", methods = ['GET', 'POST'])
def home():
    feature_form = FeatureForm()
    file_form = FileForm()
    with open ("static/final_svm_model.pkl",'rb') as pickle_file:
          model = pickle.load(pickle_file)

    if feature_form.validate_on_submit():
        sepal_length= feature_form.sepal_length.data
        sepal_width = feature_form.sepal_width.data
        petal_length = feature_form.petal_length.data
        petal_width = feature_form.petal_width.data

        data = np.array([sepal_length,sepal_width, petal_length, petal_width]).reshape(1,-1)
        prediction= model.predict(data)
        predict_result = ""

        if prediction == 0:
            predict_result = 'setosa'
        elif prediction == 1:
            predict_result =  'versicolor'
        else :
            predict_result = 'virginica'

        image_file_name = str(uuid.uuid4())
        image_file = image_file_name + ".png"
        search_image(predict_result, image_file)

        return render_template("home.html", feature_form=feature_form, file_form = file_form, result = predict_result, image_name=image_file)

    elif file_form.validate_on_submit():
        file = file_form.test_file.data #FileStorage object

        try:
            data= pd.read_csv(file,sep=' ', delimiter=r"\s+",index_col=False)
            prediction = model.predict(data)

        except Exception:
            return  "Something went worng. PLEASE CHECK THE FILE AGAIN"
        prediction = prediction.astype(str)
        prediction[prediction == '0'] = 'setosa'
        prediction[prediction == '1'] = 'versicolor'
        prediction[prediction == '2'] = 'virginica'

        prediction_file_name = str(uuid.uuid4())
        predict_result_file = prediction_file_name + ".txt"

        np.savetxt("static/prediction/"+ predict_result_file, prediction, fmt="%s")
        return redirect(url_for('predict_txt', filename=predict_result_file))

    return render_template("home.html", feature_form=feature_form, file_form = file_form)


@app.route('/getPrediction/<filename>') #
def predict_txt(filename):
     return send_from_directory('static/prediction',filename,as_attachment=True)
