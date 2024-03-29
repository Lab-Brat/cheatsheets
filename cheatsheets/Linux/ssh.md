### SSH
#### public-key authentication
* `ssh-keygen -f /path/to/key -P "" -q` -> create key
* copy key
```
ssh-copy-id -i /path/to/key user@10.10.10.10
# copy without entering password
# sshpass -p 'password' ssh-copy-id -o StrictHostKeyChecking=no -i /path/to/key root@10.10.10.10
```
* `ssh -i /path/to/private/key user@10.10.10.10` -> connect with a specified key
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
* Connect to a Linux host that has only a private IP
```                                             
  +----------+     (2) +----------+ (1)  (3) +----------+     
  | client_1 |-------->| server_1 |<-------->| client_2 |     
  +----------+         +----------+          +----------+    
 
# client_1: client from which the SSH connection will initiate.
# server_1: intermediate host with public IP that will facilitate the connection.
# client_2: client to which client_1 is connecting to.

# (1) SSH from client2 to the server and forward port 50505
ssh -R 50505:localhost:22 user@server_1

# (2) SSH from client2 to the server, and verify port existence
ssh user@server_1
ss -tulpn

# (3) SSH from the server to client_2
ssh -p 50505 user@localhost
```

* Tunnel local hugo server to client
```
  +----------+     (1) +----------+ 
  | client_1 |-------->| server_1 |
  +----------+         +----------+

# (1) SSH connect from client_1 to server_1 and map ports to localhost
ssh -L 1313:localhost:1313 user@hugo_server

# in browser: http://127.0.0.1:1313
# if the url about is availabe on the server, it will now be available on the client.
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
