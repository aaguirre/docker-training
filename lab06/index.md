# Lab 06: Clustering 

## Docker Swarm Mode:

Cluster management integrated with Docker Engine.

https://docs.docker.com/engine/swarm/


```bash
docker swarm init
```

```data
Swarm initialized: current node (vrey7wo8ljr8kgsk2r8khqyg9) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-2diegsylqrh0wzk7ot6imus33dy22odtt69rre3x6u7cb3utpo-0jiru81qgnigvh1yy6q3uwqgs 192.168.65.2:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```


```vim
docker info 
```

```vim
 Swarm: active
 NodeID: vrey7wo8ljr8kgsk2r8khqyg9
 Is Manager: true
 ClusterID: k2f4z71r11ak230nabi5u77iy
 Managers: 1
 Nodes: 1
 Orchestration:
  Task History Retention Limit: 5
```

Node list

```bash
docker node ls
```

Service list

```bash
docker service ls
```

Create Service
```bash
docker service create --name nginx -p 82  nginx
```

Service status

```bash
docekr service ps nginx
```

Service Logs
```bash
docker service logs -f nginx
```

Scale a service
```bash
docker service scale nginx=4
```

Deploy a stack of service using docker-compose
```bash
docker stack deploy --compose-file docker-compose.yml adass
```

```text
Creating network adass_default
Creating service adass_nginx
Creating service adass_app
Creating service adass_redis
```

Go to url:

http://machine-ip:80


Docker stack ls, ps, etc.

```bash
docekr stack ls
```

