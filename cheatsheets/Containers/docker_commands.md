### Docker
#### Container operations
* `docker ps` -> list currently running containers
* `docker ps -a` -> list all containers 
* `docker start <id>` -> starting container 
* `docker stop <id>` -> stopping container 
* `docker rm <id>` -> removing container 
* `docker container prune` -> remove all stopped containers 
* `docker run -d -it <image-name>` -> run container from image with terminal 
* `docker run -d -p 6000:6379 <id>` -> bind port
* `docker run -d --name special-name` -> set name 
* `docker exec -it 993ccbbb0689 /bin/bash` -> login with console 
* `docker logs <id>` -> check logs 

#### Images
* `docker images` -> list all images 
* `docker rmi <image-id>` -> delete an image 
* `docker pull fedora` -> download Fedora image 

#### Volumes
* `docker volume list` -> list all volumes
* `docker volume ls -qf dangling=true` -> list unused volumes
* `docker volume rm <vid>` -> delete volume
* `docker volume rm $(docker volume ls -qf dangling=true)` -> delete unused volumes

#### Misc
* `curl -X GET http://localhost:5000/v2/_catalog` -> list available images from local registry 
* `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name>` -> get IP address of the container 
* `docker system prune -a` -> clean all images, containers and networks
* `docker inspect nginx_reverse_proxy | grep com.docker.compose | grep -E "config|dir"` -> find compose config file location from running contianer

#### Dockerfile
* `docker build -t <image-name> .` -> build image from a Dockerfile in current directory 
* Dockerfile example
```dockerfile
FROM fedora:latest

# install rsyslog
RUN dnf -y update
RUN dnf install -y rsyslog

# copy configuration file
COPY rsyslog.conf /etc/rsyslog.conf

# run rsyslog
ENTRYPOINT ["rsyslogd", "-n"]
```
