# Server Setup and SSH Configuration

## VM configuration
---
- I use the UTM for spinning up the virtual machine
- Steps are as follows
	- Get iso from official site
	- Config the hardware requirements for the VM (CPU cores ,RAM)
	- Open UTM and boot the iso
- Remove the iso after successful boot and installation
## SSHD installation and running
---
### Verify the status of SSHD
- The sshd is the daemon which serves the ssh.
- Before further process we have to verify whether the SSHD is functioning or not using the systemctl command.
```shell
# To check status 
systemctl status sshd

#To enable 
systemctl enable sshd

# To start the sshd
systemctl start sshd
```

## Configuring for Password-less authN
---
### Generate the keys (on macbook)
- The ssh-keygen is used for the generation of the asymmetrical keys
- `-t` -> is for mentioning the type of encryption
- `-f` -> mentions the location
```shell
ssh-keygen -t ed25519 -f ./keys
```
### Get the IPaddress of the host 
- Use the following command and **look for the IPV4 address**
```shell 
ip a 
```
### Copy the keys (from macbook to the linux server)
- Use the ip of the server and hostname to copy the keys 
```shell
#ssh-copy-id -i <sourcefile> -t <desinationfile> <hostname>i@<FEDORA_IP_ADDRESS>
ssh-copy-id -i ./keys.pub -t ~/.ssh/authorized_keys hari@192.168.64.13
```

### Modifying the etc of ssh
- Navigate to the /etc/ssh/sshd_config file
- Add the following `PubkeyAuthentication yes` or uncomment it from the following file
- And make the `PasswordAuthentication no` to disable the password based authentication

> Restart the sshd after this

 ```shell
 sudo systemctl restart sshd
 ```

## Now ssh using the keys
---
- use the -i flag followed by the destination of the private key
```shell 
ssh -i keys hari@192.168.64.13
```
