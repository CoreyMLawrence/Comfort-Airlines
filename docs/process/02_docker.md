# Docker - Containerized Deployment
Historically, client deployment of developer applications has been error-prone because application developers
make assumptions about the environment that the application will be executed in. For example, the application
may require the `mariadb` Python package, but not specify which version. If the client has version 0.8.3 installed
but the application uses features introduced in 1.1.2, then the application will crash at runtime. To avoid 
environment-related deployment issues, this application is fully [containerized](https://www.ibm.com/topics/containerization).
The application is shipped with the dependencies and configurations such that it can be deployed and run without needing any
external configuration by the client. Running `docker compose up --build` is sufficient.