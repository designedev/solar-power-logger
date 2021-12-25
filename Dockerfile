FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app
ADD . /app

COPY requirements.txt requirements.txt

RUN  ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/timezone && \
     ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
     pip3 install -r requirements.txt

COPY . .
ENTRYPOINT ["python3"]
CMD ["run.py"]
