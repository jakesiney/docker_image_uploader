
FROM python:3.11

RUN pip install pipenv

COPY . /application

WORKDIR /application

VOLUME [ "/app/static/images" ]

RUN pipenv install --system --deploy

CMD [ "python", "application.py" ]