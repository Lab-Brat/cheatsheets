### SSH
#### public-key authentication
* create key
```
ssh-keygen -f /path/to/key -P "" -q
```
* copy key
```
ssh-copy-id -i /path/to/key user@10.10.10.10
# copy without entering password
# sshpass -p 'password' ssh-copy-id -o StrictHostKeyChecking=no -i /path/to/key root@10.10.10.10
```
* connect with a specified key
```
ssh -i /path/to/private/key user@10.10.10.10
```
* use keys automatically
```
vim ~/.ssh/config
# add following to config
Host github.com
        User git
        Hostname github.com
        IdentityFile /home/user/.ssh/id_rsa
```

* turn on ssh agent
```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
```

#### SSH tunnel
```
# connect from remote client to remote server
# on local client forward ephemral port 50505 to remote server
ssh -R 50505:localhost:22 user@10.10.10.10
# check open ports
ss -tl
# tunnel back through port 50505 to local client
ssh -i /home/user/.ssh/id_rsa -p 50505 user@localhost
```

#### SSH settings
* keep ssh session alive for 72 hours
```
vim ~/.ssh/config
# enter following to the config file
Host *
        ServerAliveInterval 2600
        ServerAliveCountMax 100
```
