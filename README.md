# flask_IrisData_prediction
This project shows an example of deploying a machine learning model using Flask.
A simple Scikit-learn model was build and an endpoint was created for prediciton.
 User can upload the test data file or put feature value individually. 
 
 ## Build the application
Build the image manually by cloning the Git repo.
```
$ git clone https://github.com/jyotipba/flask_IrisData_prediction.git
$ docker build -t imagename
```
## Run the container
```
$ docker run -p 8888:5000 imagename
```
