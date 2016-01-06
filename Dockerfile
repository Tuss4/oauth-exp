FROM python:3
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/

EXPOSE 5000

WORKDIR /code/oauthseed
CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]
