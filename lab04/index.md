# Lab 04: Running our application

## Docker run:

NGINX <--> *PYTHON* <--> *REDIS*

```bash 
docker run -d --name my-app -p 8080:8080 aaguirre/app
```


The application should fail, why?

```bash
docker logs my-app
```

First, we need to remove the recently created container.

```bash
docker rm my-app
```

Create the missing redis container

```bash
docker run --name redis -p 6379:6379 -d redis
```

Run the app container

```bash 
docker run -d --name my-app -p 8080:8080 --link redis:redis aaguirre/app
```

