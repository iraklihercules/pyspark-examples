FROM python:3.11

RUN apt update \
   && apt install default-jdk -qqy

RUN echo 'alias ll="ls -al"' >> ~/.bashrc

ADD src /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
