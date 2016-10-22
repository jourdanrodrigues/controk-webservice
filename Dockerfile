FROM python:3.5.2
MAINTAINER Jourdan Rodrigues

WORKDIR /project/

COPY . .
RUN pip install -r requirements.txt
RUN python manage.py compilemessages
RUN python manage.py collectstatic --no-input
