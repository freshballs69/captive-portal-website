FROM docker.io/fedora

RUN dnf install -y python3.13 python3-pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "sanic", "app:app"]