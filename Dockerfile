# Python image for xgboost
# docker build --tag ml_xgboost:latest .
# docker run -it -v `pwd`:/ml -p 8888:8888 ml_xgboost sh -c 'jupyter notebook --ip 0.0.0.0'

FROM python:2

RUN apt-get update
RUN apt-get install -y build-essential
RUN mkdir /ml
WORKDIR /ml
RUN git clone --recursive https://github.com/dmlc/xgboost
RUN cd xgboost; make -j4
RUN pip install --upgrade pip
RUN pip install numpy scipy matplotlib ipython jupyter pandas xgboost
