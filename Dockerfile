FROM centos:centos7

# System dependencies
RUN yum install -y \
        epel-release \
    && yum install -y \
        python3 python3-pip \
        python-dev build-essential \
        libsm6 libxext6 \
        curl unzip wget bzip2 \
        xvfb \
        python3-devel \
    && yum clean all

RUN yum install -y \
      libsm6 libxext6 \
      curl unzip wget bzip2 \
      xvfb \
      python3-devel

RUN yum install gcc -y

RUN yum install make -y

RUN yum install automake libtool -y

RUN yum install gcc-c++ -y

ADD ./requirements.txt /app/requirements.txt

WORKDIR /app

EXPOSE 5000

RUN pip3 install -r requirements.txt

ADD . /app

CMD python3 main.py
