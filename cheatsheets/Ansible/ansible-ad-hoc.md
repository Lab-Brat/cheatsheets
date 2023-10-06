### Ad Hoc Commands
#### Get Informnation
* `ansible staging -m ping` -> check connectivity to host 
* `ansible all -m setup` -> check os info 
* `ansible-doc -l | grep aws*` -> check ansible installed module information 
* `ansible-inventory --list` or `--graph` -> get inventory relationships

#### Run Commands
* `ansible all -m shell -a 'hostnamctl'` -> run ad hoc command with env 
* `ansible all -m command -a 'hostnamctl'` -> run ad hoc command without env, default behaviour if module is not specified
**NOTE** `shell` also supports <, >, |, and & operation, while `command` does not.

#### Copy and remove
* `ansible all -m copy -a 'src=halo.txt dest=/home mode=777' -b` -> copy to 
* `ansible all -m file -a "path=/home/halo.txt state=absent" -b` -> remove from 

#### URL and URI
* `ansible all -m get_url -a "url=<link> dest=/home" -b` -> download file from url
* `ansible all -m uri -a "url=https://gnu.org return_content=yes"` -> check uri connectivity on host 

#### Package management
* `ansible all -m yum -a "name=tmux state=installed"` -> install packages with yum 
* `ansible all -m yum -a "name=kernel-tools state=latest update_only=yes"` -> update packages with yum 

#### Services
* `ansible all -m service -a "name=httpd state=started"` -> start service 

#### User and Group management
* `ansible all -b -m group -a "name=admins state=present"` -> create an admin group 
* `ansible all -b -m user -a "name=labbrat group=adminz createhome=yes generate_ssh_key=yes"` -> add user to admin group 

#### Extra Options
* `ansible all -a 'hostname' -f 20/` -> increase amount (20) of parallel run forks 
* `ansible all -b -a "service ntpd restart" --limit "*.4"` -> limit connection to a certain host 
