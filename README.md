# TODO List

<br />

The following project is a system that configures a bash client to a local python server hosted within a docker environment. 

<br />

## How to use it

<br />

1.    Clone the project.
2.    Within an environment that can run docker, execute the start.sh file.

## Assumptions

<br />

1.    The docker environment port forwards traffic on 8081 within the host to the application process.
2.    The client and the docker container run on the same host.
3.    To use the CLI its important that the CSV formatting is respected

## Example commands for the client
1.    add_task buy milk,buy eggs,go to the bank,brush my teeth
2.    delete_task buy milk
3.    get_all_tasks
