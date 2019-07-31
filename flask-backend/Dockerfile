FROM python:3.6.8
ADD . /flask-backend
WORKDIR /flask-backend
RUN apt-get update -y
RUN apt-get install -y libopencv-dev
RUN pip install -r requirements.txt \
  opencv-python==3.4.0.14
