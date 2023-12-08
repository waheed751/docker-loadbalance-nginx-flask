FROM python:3.9-alpine
WORKDIR /app
COPY . /app

RUN apk add --no-cache --update build-base \
    && pip install flask \
    && apk del build-base

EXPOSE 5000

CMD ["python", "app.py"]
