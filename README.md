# TODO List

<br />

The following project is a system that configures a bash client to a local python server hosted within a docker environment. 

<br />

## How to use it

<br />

1.    Clone the project.
2.    Within an environment that can run docker, execute the start.sh file.
3.    If the terminal hangs, close it or open a new terminal.
4.    Enter the docker container using a command like 'docker exec -it <container name> /bin/bash'.
5.    Within the docker container, go into /root and then run 'pip install -r requirements.txt'.
6.    Within the root, run python app.py.
7.    From a CLI that supports /bin/bash, run and use the client by executing the client.sh file.

## Assumptions

<br />

1.    The docker environment port forwards traffic on 8081 within the host to the application process.
2.    The client and the docker container run on the same host.
