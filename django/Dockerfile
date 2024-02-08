FROM ubuntu:latest

COPY . /home/

WORKDIR /home/charge/

RUN apt update -y && apt upgrade -y

RUN apt install python3-pip -y

RUN pip3 install -r /home/charge/requirements.txt

RUN pip3 install tzdata

CMD python3 manage.py makemigrations

CMD python3 manage.py migrate

CMD python3 manage.py runserver 0.0.0.0:8000
