FROM python:3.8-alpine


RUN addgroup django && \
    adduser -D -h /app -G django django

COPY service /app
COPY requirements.txt /tmp

WORKDIR /app

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt

USER django

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
