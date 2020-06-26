#!/bin/bash

echo "Welcome to the TODO list manager. 
    To delete tasks, use: delete_task arg1,arg2, ... ,argn 
    To add tasks, use: add_task arg1,arg2, .., argn 
    To get all the tasks, use: get_all_tasks
    To exit: press q

    Please remember to provide arguments as a csv string
    "

main() {
    while true
    do
        read -p "Command: " user_input 
        command=`echo $user_input | cut -d ' ' -f1`
        if [[ $command == "add_task" ]]; then
            tasks=`echo $user_input | cut -d ' ' -f2-`
            if [[ $tasks == "add_task" ]]; then
                echo "Please provide tasks as csv seperated command line arguments"
            else
                IFS=","
                for task in $tasks; do
                    curl -s -L -d "task=$task" http://127.0.0.1:8081/api/tasks -X POST >> /dev/null
                done
                IFS=" "
                curl -L http://127.0.0.1:8081/api/tasks
            fi
        elif [[ $command == "delete_task" ]]; then
            tasks=`echo $user_input | cut -d ' ' -f2-`
            if [[ $tasks == "delete_task" ]]; then
                echo "Please provide tasks as csv seperated command line arguments"
            else
                IFS=","
                for task in $tasks; do
                    task=${task// /%20}
                    curl -s -L  http://127.0.0.1:8081/api/tasks?task=$task -X DELETE >> /dev/null
                done
                IFS=" "
                curl -L http://127.0.0.1:8081/api/tasks
            fi
        elif [[ $command == "get_all_tasks" ]]; then
            curl -L http://127.0.0.1:8081/api/tasks
        elif [[ $command == "q" ]]; then
            exit 0
        else
            echo "
            Please provide the proper command
            To delete tasks, use: delete_task arg1 arg2 ... argn 
            To add tasks, use: add_task arg1 arg2 .. argn 
            To get all the tasks, use: get_all_tasks
            To exit: press q

            Please remember to provide arguments as a csv string"
        fi
    done
}

main