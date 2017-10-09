FROM python:3

ARG STAGE=development
ARG RELEASE=1.0

WORKDIR /usr/src/app

RUN pip install pyramid pyramid_jinja2 redis

COPY app /usr/src/app

COPY puppy.jpg /var/puppy.jpg

EXPOSE 8080

CMD [ "python", "/usr/src/app/app.py" ]
