FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        ca-certificates \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python3-tk && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/
RUN git clone --recursive https://github.com/ddfabbro/DNN-Pruning.git

ENV CAFFE_ROOT /usr/src/DNN-Pruning/caffe/
WORKDIR $CAFFE_ROOT
COPY Makefile.config .

RUN for req in $(cat python/requirements.txt);do pip3 install $req; done && \
    pip3 install protobuf --upgrade && \
    pip3 install python-dateutil --upgrade && \
    pip3 install protobuf==3.0.0b2 && \
    pip3 install easydict && \
    pip3 install scikit-learn && \
    pip3 install termcolor && \
    make -j"$(nproc)" && \
    make pycaffe

ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

WORKDIR /usr/src/DNN-Pruning/
