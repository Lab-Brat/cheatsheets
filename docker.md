# Docker
### basic container operations
* list currently running containers and all
```
docker ps
docker ps -a
```
* run container from image with terminal
```
docker run -d -it <image-name>
```
* starting, topping and removing
```
docker start <id>
docker stop <id>
docker rm <id>
docker container prune
```
* bind port
```
docker run -d -p 6000:6379 redis:4.0
```
* check logs
```
docker logs <id>
docker logs
```
* run with specific name
```
docker run -d --name special-name
```
* login with console
```
docker exec -it 993ccbbb0689 /bin/bash
```

* list available images from local registry
```
curl -X GET http://localhost:5000/v2/_catalog
```
