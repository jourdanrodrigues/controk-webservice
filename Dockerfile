FROM python:3.5.2
MAINTAINER Jourdan Rodrigues

RUN apt-get update -y && apt-get install -y gettext

WORKDIR /project/

COPY . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input && python manage.py compilemessages