FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask

COPY app.py ./
COPY templates ./templates

CMD [ "python3" , "/app.py" ]
