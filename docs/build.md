# Building the Program
This application uses Docker to publish the application with its dependencies and environment settings.
It uses two dockers: a Python 3.10 docker for the application and a MariaDB docker for the database,
which are connected over the default bridge network. Below are a few common commands from
[the docker cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).

- Build and deploy containers: `docker compose up --build --detach`
- Build and deploy container with [hot reload](https://learn.microsoft.com/en-us/visualstudio/debugger/hot-reload?view=vs-2022): `docker compose watch` (recommended if doing live development)
- List containers by name and details: `docker ps`
- Connect to container via commandline: `docker exec -it <CONTAINER_NAME>`
- Stop containers: `docker compose down`