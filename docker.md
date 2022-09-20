### Docker
#### Basic container operations
* list currently running containers ```docker ps```
* list all containers ```docker ps -a```
* run container from image with terminal ```docker run -d -it <image-name>```
* starting container ```docker start <id>```
* stopping container ```docker stop <id>```
* removing container ```docker rm <id>```
* remove all stopped containers ```docker container prune```
* bind port ```docker run -d -p 6000:6379 <id>```
* check logs ```docker logs <id>```
* set name ```docker run -d --name special-name```
* login with console ```docker exec -it 993ccbbb0689 /bin/bash```

#### Registry
* list available images from local registry ```curl -X GET http://localhost:5000/v2/_catalog```

#### Dockerfile
* build image from a Dockerfile in current directory ```docker build -t <image-name> .```
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
