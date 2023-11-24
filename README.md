# Nginx for load balancing Python Flask application over docker containers
This example illustrates the process of constructing a custom Docker image for a Flask application. Subsequently, it employs Docker Compose to initiate four containers for the Flask application and another container running Nginx,
which is a load balancer for handling HTTP requests.

## Prerequisite 
To successfully run this example, ensure that the following prerequisites are installed.
- docker
- docker-compose
## Flask application 
Folder `flask_app` contains `app.py` file, which outputs the IP address of the machine/container running this code. 

### Building flask application docker image
Use the `Dockerfile` available in the `flask_app` folder to build a local docker image. Assuming we want to create an image named my-app, use the following command:
<pre>
docker build . -t my-app
</pre>

## Nginx for load balancing 
We will use docker-compose to run four containers for the flask_app using the image we created in the previous step. Also, one Nginx container will be launched, and the `nginx.conf` file will be mapped to the container. The file `docker-compose.yml' will be used to 
run this application. 
<pre>
docker-compose up
</pre>
You can check the running containers using:
<pre>
docker ps 
</pre>

## Testing the application 
Discover the IP address of the Nginx container and open it in the browser to check the application. 
Retrieve the Nginx container ID and then use `docker inspect` to pinpoint the container's IP address. By refreshing the Nginx IP in the browser multiple times, you will observe varying IP addresses being displayed. You can also use `curl` to test the application!

## Loom Video
Loom video for step-by-step instructions on running and testing the application with `curl`. The video provides a visual guide that demonstrates the necessary processes.
[![Loom Video](https://cdn.loom.com/sessions/thumbnails/c464b64f81e848ea8c39c4199846b6bc-with-play.gif)](https://www.loom.com/share/c464b64f81e848ea8c39c4199846b6bc?sid=2fd2f6db-d709-4c73-a691-e6a4f65b2c09)
