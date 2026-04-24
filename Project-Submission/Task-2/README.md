# Task 2: Docker Installation and Application Deployment
---
### Steps for the installation of Docker 

-  Find out what package manager does your server uses `Ubuntu - apt , RH - dnf , Arch - pacman` or what flavour of Linux is your server
- You can use the following command to find out what the distro is 
	```cat /etc/os-release | grep "NAME"```
- Here in my case I use the Fedora which is based on RedHat so it has `dnf` as it's package manager.
-  The best way to install Docker is by referring to the documentation of how it is done. [Documentation](https://docs.docker.com/engine/install/fedora/)
#### Installation commands

```shell
# Installing docker 
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Enabling/Starting the Docker Daemon
sudo systemctl enable --now docker

# Verification after the insallation
docker --version
sudo docker run hello-world

```

> NOTE : By default you need **sudo** privileges to run docker commands.

```shell
# To run without sudo create and add the user to the docker group
sudo usermod -aG docker $USER
newgrp docker
```

### Building a docker file to host the static file and running it in a container

- Docker workflow is `Dockerfile -> Container Image -> Container`
- Dockerfile has some instructions like Base OS, commands to be run, Ports to be exposed etc...

> The goal is to host this following index.html file

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Deployment</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f6f9; font-family:Arial, sans-serif; display:flex; justify-content:center; align-items:center; height:100vh;">

    <div style="background:#ffffff; padding:40px; border-radius:10px; box-shadow:0 4px 15px rgba(0,0,0,0.1); text-align:center; width:90%; max-width:500px;">
        
        <h1 style="color:#2c3e50; margin-bottom:20px;">
            🚀 Successfully Deployed in Docker
        </h1>
        
        <p style="color:#555; font-size:16px; margin-bottom:15px;">
            This application is now running inside a Docker container.
        </p>
        
        <p style="color:#333; font-size:15px; background:#eef2ff; padding:10px; border-radius:6px;">
            📌 Task Submission: This deployment demonstrates successful containerization and execution of the application using Docker.
        </p>

        <p style="margin-top:20px; font-size:12px; color:#888;">
            Deployment Status: Active & Running
        </p>

    </div>

</body>
</html>
```

- I made two approaches to host the following static file, both has their own advantages
	- Using the ngnix as base image
	- Using the busybox as base image
	
- **NGINX** : More functional, has additional features like Reverse proxy, TLS, etc..
- **BUSYBOX** : Has httpd and extremely lighter when compared to the `nginx:alpine`

> Both the docker files has simple layers choosing a base image, copying the static file to the image's filesystem for hosting and exposing the port
####  NGINX DOCKERFILE

```Dockerfile
FROM nginx:alpine

LABEL version="nginx"

COPY ./index.html /usr/share/nginx/html/index.html

EXPOSE 8000
```

#### BUSYBOX DOCKERFILE

```Dockerfile
FROM busybox:stable

LABEL version="Busybox" 

COPY ./index.html /www/index.html

CMD ["httpd", "-f", "-p", "8000", "-h", "/www"]
```

#### Building the docker image
 
> It is the process of creating a docker image from a docker file

```shell
# syntax
# docker build -t <name:tag> <path/to/Dockefile>

docker build -t staticserver:0 .
```

### Running the container

> It is the process of turning a docker image to a running instance `the container`

```shell 
# To list the images
docker images

# To run a container
 docker run --name=server-label -d -p 8000:8000 statiscserver:0 

#After running this you can access the container in the http://localhost:8000

#List the running containers
docker ps 
```

> The run command breakdown
- **--name** : is used to name the container
- **-d** : to run the container in detached mode (runs in bg)
- **-p** : binding container's port 8000 to host's 8000
- **staticserver:0** : name of the image


