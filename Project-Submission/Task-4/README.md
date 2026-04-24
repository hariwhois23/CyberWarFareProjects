# Secure monitoring logs by restricting access to a dedicated user.

## Command to create the user
---
####  The useradd command is used to create a user

```shell
sudo useradd monitor_user
```

#### To verify if the user has been created `cat` the following file /etc/passwd

```shell
sudo cat /et/passwd | grep monitor_user
```

#### Add user to the docker group - sudo free
```shell
sudo usermod -aG docker monitor_user
```
## Creating and setting the ownership of the directory
---
#### Creating the directory
```shell
sudo mkdir -p /opt/container-monitor/logs
```
- The -p flag is used to create nested directory
#### Setting the ownership for the following directory
``` shell
sudo chown -R monitor_user:monitor_user /opt/container-monitor
```
- To verify use `ls -ltr`

#### Restricting the access for the directory
```shell
sudo chmod 700 /opt/container-monitor
```
 - 700 indicates the permission
	 - 7 -> user
		 -  1 1 1 -> r w x 
	 - 0 -> group 
	 - 0 -> others
