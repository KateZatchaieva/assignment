FROM python:latest

MAINTAINER k.zatchaieva@gmail.com

RUN mkdir /automation

COPY ./jsonplaceholder_assignment /automation/jsonplaceholder_assignment
COPY ./setup.py /automation/setup.py

WORKDIR /automation
RUN python3 setup.py install
WORKDIR /automation/jsonplaceholder_assignment
ENTRYPOINT pytest --html=./report/report.html