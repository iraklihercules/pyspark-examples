FROM python:3.11

RUN apt update

ADD src /app
WORKDIR /app

CMD ["tail", "-f", "/dev/null"]
