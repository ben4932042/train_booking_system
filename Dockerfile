FROM amd64/python:3.6-slim

ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install
RUN apt-get update -y &&  apt-get install curl -y

CMD ["python", "main.py"]
