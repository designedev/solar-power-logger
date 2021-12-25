FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app
ADD . /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENTRYPOINT ["python3"]
CMD ["run.py"]
