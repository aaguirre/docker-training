# Lab 02: Creating images

## Dockerfiles:


Clone the Lab's repo
```
git clone https://github.com/aaguirre/docker-training.git
```

```vim
FROM python:3

ARG STAGE=development
ARG RELEASE=1.0

WORKDIR /usr/src/app

RUN pip install pyramid pyramid_jinja2 redis

COPY app /usr/src/app

COPY puppy.jpg /var/puppy.jpg

EXPOSE 8080

CMD [ "python", "/usr/src/app/app.py" ]
```

[python base image](https://github.com/docker-library/python/blob/cf179e4a7b442b29d85f521c2b172b89ef04beef/3.6/jessie/Dockerfile)


```bash
docker build -t app:lab02 .
```

```bash
docker image ls

REPOSITORY    TAG    IMAGE ID     CREATED       SIZE
app           lab02  1de089b53a65 1 minute ago  707MB
```


## Options

```bash
docker build --help
```

```bash
docker build -t app:lab02 --build-arg STAGE=testing --build-arg RELEASE=2.0 .
```

