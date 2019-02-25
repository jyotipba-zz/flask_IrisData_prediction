#- sepal length in cm\n        - sepal width in cm\n        - petal length in cm\n        - petal width in cm\n
#array(['setosa', 'versicolor', 'virginica']
#And the convenience validate_on_submit will check if it is a POST request and if it is valid.
from flask_wtf import FlaskForm
from wtforms import DecimalField,SubmitField
from flask_wtf.file import FileField, FileRequired,FileAllowed
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired

class FeatureForm(FlaskForm):
    sepal_length = DecimalField("sepal length", validators =[DataRequired()] )
    sepal_width = DecimalField("sepal width",  validators =[DataRequired()])
    petal_length = DecimalField("petal length",  validators =[DataRequired()])
    petal_width = DecimalField("petal width",  validators =[DataRequired()])
    submit = SubmitField("Predict")

class FileForm(FlaskForm):
    test_file = FileField(validators=[FileRequired(), FileAllowed(['txt'])])
    submit = SubmitField("Upload file")