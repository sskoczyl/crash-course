FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend/

COPY . /backend/

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev libressl-dev libffi-dev \
    && apk add postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
