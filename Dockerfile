FROM python:3.8
COPY . .
RUN apt-get -y update \
    && pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "./manage.py"]