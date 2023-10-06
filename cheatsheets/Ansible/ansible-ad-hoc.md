### Ad Hoc Commands
#### Get Informnation
* check connectivity to host ```ansible staging -m ping```
* check os info ```ansible all -m setup```  
* check ansible installed module information ```ansible-doc -l | grep aws*```  
* get inventory relationships ```ansible-inventory --list``` or ```--graph```

#### Run Commands
* run ad hoc command with env ```ansible all -m shell -a 'hostnamctl'```
* run ad hoc command without env ```ansible all -m command -a 'hostnamctl'```, default behaviour if module is not specified
**NOTE** `shell` also supports <, >, |, and & operation, while `command` does not.

#### Copy and remove
* copy to ```ansible all -m copy -a 'src=halo.txt dest=/home mode=777' -b```
* remove from ```ansible all -m file -a "path=/home/halo.txt state=absent" -b```  

#### URL and URI
* download file from url ```ansible all -m get_url -a "url=<link> dest=/home" -b```  
* check uri connectivity on host ```ansible all -m uri -a "url=https://ya.ru return_content=yes"```  

#### Package management
* install packages with yum ```ansible all -m yum -a "name=tmux state=installed"```  
* update packages with yum ```ansible all -m yum -a "name=kernel-tools state=latest update_only=yes"```

#### Services
* start service ```ansible all -m service -a "name=httpd state=started"```  

#### User and Group management
* create an admin group ```ansible all -b -m group -a "name=admins state=present"```
* add user to admin group ```ansible all -b -m user -a "name=labbrat group=adminz createhome=yes generate_ssh_key=yes"```

#### Extra Options
* increase amount (20) of parallel run forks ```ansible all -a 'hostname' -f 20/```
* limit connection to a certain host ```ansible all -b -a "service ntpd restart" --limit "*.4"```
