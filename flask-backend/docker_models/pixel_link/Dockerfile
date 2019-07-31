# docker run --runtime=nvidia -it --rm -v /home/jaeyub/docker_configs/test_images:/test_images --name pixel_link_container pixel_link
# FROM ubuntu:16.04
# FROM conda/miniconda2
# FROM nvidia/cuda:9.0-base-ubuntu16.04
# ADD . /pixel_link_workdir
# WORKDIR /pixel_link_workdir
# RUN apt-get update
# RUN apt-get install -y git wget unzip vim
# RUN git clone https://github.com/circulosmeos/gdown.pl.git
# RUN ./gdown.pl/gdown.pl https://drive.google.com/file/d/19mlX5W8OBalSjhf5oTTS6qEq2eAU8Tg9/edit pixel_link_vgg_4s.zip
# RUN unzip pixel_link_vgg_4s.zip

# RUN wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh
# RUN bash Anaconda2-4.2.0-Linux-x86_64.sh -b -p /home/soft/anaconda
# RUN rm Anaconda2-4.2.0-Linux-x86_64.sh
# ENV PATH=/home/soft/anaconda/bin:$PATH
# RUN conda update conda
# RUN conda env create --file pixel_link_env.yml

# RUN git clone https://github.com/ZJULearning/pixel_link.git
# WORKDIR /pixel_link_workdir/pixel_link
# RUN git clone https://github.com/dengdan/pylib.git
# ENV PYTHONPATH=${PYTHONPATH}:/pixel_link/pylib/src:$PYTHONPATH

# FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu16.04
# ADD . /pixel_link_workdir
# WORKDIR /pixel_link_workdir
# RUN apt-get update && apt-get install -y \
# 	wget \
# 	vim \
# 	bzip2 \
#     unzip \
#     git \
#     build-essential \
#     curl

#Downgrade CUDA, TF issue: https://github.com/tensorflow/tensorflow/issues/17566#issuecomment-372490062
# RUN apt-get install --allow-downgrades -y libcudnn7=7.0.5.15-1+cuda9.0

#Install MINICONDA
# ENV LATEST_CONDA "4.5.1"
# ENV PATH="/root/anaconda2/bin:${PATH}"

# RUN curl --silent -O https://repo.continuum.io/archive/Anaconda2-2019.03-Linux-x86_64.sh \
# && bash Anaconda2-2019.03-Linux-x86_64.sh -b -p /root/anaconda2

# RUN conda env create --file pixel_link_env.yml

# RUN git clone https://github.com/circulosmeos/gdown.pl.git
# RUN ./gdown.pl/gdown.pl https://drive.google.com/file/d/19mlX5W8OBalSjhf5oTTS6qEq2eAU8Tg9/edit pixel_link_vgg_4s.zip
# RUN unzip pixel_link_vgg_4s.zip

# RUN git clone https://github.com/ZJULearning/pixel_link.git
# WORKDIR /pixel_link_workdir/pixel_link
# RUN git clone https://github.com/dengdan/pylib.git
# ENV PYTHONPATH=${PYTHONPATH}:/pixel_link_workdir/pixel_link/pylib/src:$PYTHONPATH


# apt update && apt install -y libsm6 libxext6
# apt-get install -y libxrender-dev

# docker run --runtime=nvidia -it --rm -v /home/jaeyub/docker_configs/test_images:/test_images --name pixel_container pixel_link bash

FROM tensorflow/tensorflow:1.2.0-devel-gpu
RUN mkdir /pixel_link_workdir
WORKDIR /pixel_link_workdir
RUN apt-get update && apt-get install -y \
	wget \
	vim \
  unzip \
  git \
  build-essential \
  cmake \
  pkg-config \
  libswscale-dev \
  libtbb2 \
  libtbb-dev \
  libjpeg-dev \
  libpng-dev \
  libtiff-dev \
  libjasper-dev \
  libavformat-dev \
  libpq-dev \
  python-setproctitle \
  python-matplotlib

RUN git clone https://github.com/circulosmeos/gdown.pl.git \
&& ./gdown.pl/gdown.pl https://drive.google.com/file/d/19mlX5W8OBalSjhf5oTTS6qEq2eAU8Tg9/edit pixel_link_vgg_4s.zip \
&& unzip pixel_link_vgg_4s.zip \
&& rm pixel_link_vgg_4s.zip

#RUN git clone https://github.com/ZJULearning/pixel_link.git \
RUN git clone https://github.com/sungjune-p/pixel_link.git \
&& cd /pixel_link_workdir/pixel_link \
&& git clone https://github.com/dengdan/pylib.git
ENV PYTHONPATH=${PYTHONPATH}:/pixel_link_workdir/pixel_link/pylib/src:$PYTHONPATH

RUN wget https://github.com/opencv/opencv/archive/2.4.13.3.zip \
&& unzip 2.4.13.3.zip \
&& mkdir opencv-2.4.13.3/cmake_build \
&& cd opencv-2.4.13.3/cmake_build \
&& cmake -D WITH_TBB=ON \ 
      -D WITH_OPENMP=ON \
      -D WITH_IPP=ON \
      -D CMAKE_BUILD_TYPE=RELEASE \
      -D BUILD_EXAMPLES=OFF \
      -D WITH_NVCUVID=ON \
      -D WITH_CUDA=ON \
      -D BUILD_DOCS=OFF \
      -D BUILD_PERF_TESTS=OFF \
      -D BUILD_TESTS=OFF \
      -D WITH_CSTRIPES=ON \
      -D WITH_OPENCL=ON .. \
&& make install \
&& rm /pixel_link_workdir/2.4.13.3.zip \
&& rm -r /pixel_link_workdir/opencv-2.4.13.3

RUN pip uninstall -y tensorflow \
&& pip install --upgrade tensorflow-gpu==1.2.0 \
                          tensorflow==1.2.0 \
                          cython

WORKDIR /pixel_link_workdir/pixel_link

#ENTRYPOINT /pixel_link_workdir/pixel_link/scripts/test.sh 0 /pixel_link_workdir/conv3_3/model.ckpt-38055 /test_images/