FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install Flask==2.3.3
EXPOSE 5000
CMD ["python", "app.py"]