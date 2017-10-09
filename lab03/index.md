# Lab 03: Push your images

## Docker Hub:

```bash 
docker image ls
```

```bash
docker tag app:latest aaguirre/app:blabla
```

```bash
docker push aaguirre/app:blabla
```

```bash
The push refers to a repository [docker.io/aaguirre/app]
c77a09d298dd: Layer already exists
0e00865b3b40: Layer already exists
d9af6695b44f: Layer already exists
cfc14c972e9a: Layer already exists
c7e725986a0a: Layer already exists
c22e5f96f9b4: Layer already exists
f173c06848be: Layer already exists
1e96ffb4a81f: Layer already exists
7381522c58b0: Layer already exists
ecd70829ec3d: Layer already exists
d70ce8b0dad6: Layer already exists
18f9b4e2e1bc: Layer already exists
```


## Create a private repository

https://docs.docker.com/registry/deploying/

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```
