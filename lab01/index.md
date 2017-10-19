# Lab 01: Docker basics

## Installation:


https://docs.docker.com/engine/installation/

```vim
yum install -y yum-utils device-mapper-persistent-data lvm2
```

```vim
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

```vim
yum install docker-ce
```

```vim
systemctl start docker
```

```vim 
docker run hello-world
```


## Basic commands:

```vim
docker info
```

```vim
docker version
```

List docker images
```vim 
docker image ls             (see docker image --help)
```

List running docker containers
```vim
docker container ls         (see docker container --help)
```

Pull a new image from Docker Hub.
```vim
docker image pull nginx
```

Run NGINX container 
```bash
docker run --name my-nginx -d -p 8080:80 nginx
```

Open browser at: 

[http://virtual-machine-ip:8080](http://virtual-machine-ip:8080)

Remove NGINX container
```
docker rm -f my-nginx
```


