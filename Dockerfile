
FROM python:3.11

COPY . /app

WORKDIR /app

VOLUME [ "/app/static/images" ]

RUN pip install Flask==1.0.2

EXPOSE 5000

CMD [ "python", "app.py" ]