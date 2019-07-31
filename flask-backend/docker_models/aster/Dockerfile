FROM tensorflow/tensorflow:1.4.0-devel-py3
RUN mkdir /aster_workdir
WORKDIR /aster_workdir
RUN apt-get update && apt-get install -y \
  wget \
  git \
  vim \
  unzip \
  cmake \
  libcupti-dev \
  build-essential

RUN git clone https://github.com/sungjune-p/aster.git \
&& cd aster/experiments/demo \
&& wget https://github.com/bgshih/aster/releases/download/v1.0.1/model-demo.zip \
&& unzip model-demo.zip \
&& rm model-demo.zip

RUN pip install --upgrade pip \
&& pip install protobuf tqdm editdistance Pillow pymongo

RUN cd aster/c_ops \
&& ./build.sh

RUN wget https://github.com/google/protobuf/releases/download/v2.6.1/protobuf-2.6.1.tar.gz \
&& tar xzf protobuf-2.6.1.tar.gz \
&& cd protobuf-2.6.1 \
&& ./configure \
&& make \
&& make check \
&& make install \
&& ldconfig

RUN protoc aster/protos/*.proto --python_out=.

ENV PYTHONPATH=${PYTHONPATH}:/aster_workdir/aster/:$PYTHONPATH

#ENTRYPOINT python3 aster/demo.py
