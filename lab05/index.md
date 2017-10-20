# Lab 05: Orchestration

## Docker compose:

Compose is a tool for defining and running multi-container Docker applications

https://docs.docker.com/compose/

Install Docker Compose 
```
curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /bin/docker-compose
chmod +x /bin/docker-compose
```

```
docker-compose --version
```

                                     
                       +------------+
                       |            |
                       |    NGINX   |
                       |            |
                       +------+-----+
                              |      
                              |      
                       +------|-----+
                       |            |
                       |    APP     |
                       |            |
                       +------+-----+
                              |      
                              |      
                       +------|-----+
                       |            |
                       |   Redis    |
                       |            |
                       +------------+

Open docker-compose.yml

```yaml
version: '2'

services:

  app:
    image: aaguirre/app:latest
    build:
      context: ../lab02/
      args:
       - STAGE=testing
       - RELEASE=3.0
    container_name: app
    links:
      - redis:redis
    networks:
      - default
    mem_limit: 100m
    restart: always
    ports:
      - "8080:8080"
    volumes:
      - ./puppy.jpg:/var/puppy.jpg

  redis:
    image: redis:alpine
    container_name: redis
    ports:
      - "6379:6379"
    networks:
      - default
    mem_limit: 20m
    restart: always

  nginx:
    image: nginx:alpine
    container_name: nginx
    command: ["nginx", "-g", "daemon off;"]
    links:
      - app:app
    ports:
      - "80:80"
    networks:
      - default
    mem_limit: 10mb
    restart: always
    volumes:
     - ./nginx.conf:/etc/nginx/conf.d/default.conf

networks:
  default:
    driver: bridge
```


Run docker compose 

```bash
docker-compose up -d
```

