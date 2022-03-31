#FROM python:3.10 #better for prod
FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./*.py /backend/

EXPOSE 8080
CMD gunicorn --chdir /backend backend:app -b :8080 -w 1 --threads 2 --timeout 10
