# Monitor container resource usage and log CPU and memory usage with timestamps automatically.

## BASH script

```bash
#!/bin/bash

LOG_PATH="/opt/container-monitor/logs/container.log"
DATE=$(date "+%c")
CONTAINER_NAME="f3b77687d308"

STATE=$(docker inspect -f '{{.State.Status}}' "$CONTAINER_NAME" 2>/dev/null)

if [[ "$STATE" != "running" ]]; then
  if [[ -z "$STATE" ]]; then
    echo "Time: $DATE | ERROR: Container '$CONTAINER_NAME' does not exist."
  else
    echo "Time: $DATE | ERROR: Container '$CONTAINER_NAME' is $STATE (not running)."
  fi
  exit 1
fi

docker stats --no-stream --format "Time: $DATE | Container: {{.Name}} | MEMORY: {{.MemUsage}} | CPU: {{.CPUPerc}}" $CONTAINER_NAME

```

> Explaining the bash script
- `date "+%c"` To get the timestamp
- `LOG_PATH` is the path where the logs has to be stored 
- `CONTAINER_NAME` is hardcoded and also could be replaced with $1 if passing as an argument
- `docker inspect` gets the current status of the container
- `IF` conditions are used to identify and separate the current status of the container and exit if any of the following case is found.
	- **Does not exist** 
	- **Not running**
- `docker stats` is the actual logger to log the memory and cpu consumption 

> Executing the script
- Create the file with the extension sh with the following code
- Add executable permission to the script and save it 
- ./<script_name> to run it

## Adding the script to the cron

> Before adding the script to the crontab, check whether the cron's daemon is running or not by using the following command ` sudo systemctl crond`

**If the service is not active then turn it on by using the following command**
 ```shell
sudo systemctl start crond
sudo systemctl enable crond
 ```

#### Cron syntax : to know more here's the link to my [blog](https://medium.com/@prasaths/crontab-a-complete-walkthrough-of-automation-and-scheduling-part-1-7f374e2b1659)

#### Cron setup 
---
- Use the following command to edit the cron tab

```shell
crontab -e
```

- To execute the following script every minute you need these three,
	- The cron syntax for every minute
	- The **absolute path** of the shell script
	- where the output has to be redirected 

```shell 
* * * * * /Users/hariprasath/Desktop/CyberWarFareProjects/Project-Submission/Task-3 >> /opt/container-monitor/logs/container.log
```

- We can cat the `container.log` to check for the log

- To trouble shoot cron use the command to check the Logs for the ongoing cron-job
```shell
 journalctl -u crond 
```
