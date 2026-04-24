#  Firewall Configuration

## Later I found out that this could be easily dealt by editing the /etc/ file of ufw due to time constraints I made this approach

## Installing the UFW
--- 
- using the builtin package manager `dnf` for the installation of the 
```shell 
sudo dnf install ufw -y
```

- Check if the `firewalld`  daemon is running if yes disable it to enable the ufw
- The firewalld intervenes with the functioning of the ufw so it is better to disable it 
```shell 
sudo systemctl stop firewalld 
sudo systemctl disable firewalld 
```

### Start the ufw's daemon process now 
```shell 
systemctl enable ufw 
```

## Restricting the services 
---
#### Allowing ssh from only a single ip
```shell 
sudo ufw allow from 192.168.0.2 to any port 22 proto tcp
```

#### Allowing the http access
```shell 
sudo ufw allow 80/tcp
```
#### Allowing PORT 8000
```shell
sudo ufw allow 8000/tcp
```

### Final add-on
---
#### Denying all incoming and all outgoing by default
```shell 
sudo ufw default deny incoming 
sudo ufw default allow outgoing
```

#### Enabling the firewall
```shell 
sudo ufw --force enable
```

### Verification
---
#### Use to verify a table with configs appear
```shell
sudo ufw status numbered
```

#### To reset
- If any problem found and has to restart the process from the beginning use the reset
```shell 
sudo ufw reset
```
