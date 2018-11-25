FROM python:3.4-jessie

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
COPY docker-entrypoint.sh /usr/src/app/app

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD ["-w", "2", "-b", ":8888", "app:app"]

