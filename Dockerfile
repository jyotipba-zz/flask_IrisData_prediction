FROM python:3
MAINTAINER Jyoti Bartaula "jyoti.bartaula@gmail.com"
WORKDIR /app
COPY requirements.txt requirements.txt
# Copy the app directory contents into the container at /app
COPY app /app
# ENV FLASK_APP app.py
RUN pip install -r requirements.txt
RUN pip install flask gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
