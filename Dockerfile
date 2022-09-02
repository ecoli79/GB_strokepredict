FROM python:3.7
MAINTAINER Denis Impolitov "impol@yandex.ru"
RUN mkdir /app
WORKDIR /app
COPY . .
VOLUME /app/app/models
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./app/app.py"]
