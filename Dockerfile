FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=development
    
RUN python3 --version
RUN pip3 --version

WORKDIR /app
ADD . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get install openssl

EXPOSE 3000

CMD [ "python3", "app.py"]