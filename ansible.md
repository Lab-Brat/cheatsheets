# Ansible

#### Ansible Core
* Definition: cli tool that underlies all Ansible, comprises of 4 parts:
  * cli - ansible, ansible-playbook, ansible-doc and other cli tools
  * language - yaml
  * framework - allows plugins to be installed from Automation Hub and Galaxy
  * functions - conditionals, blocks, includes, loops and other Ansible imperatives

#### Ansbile Basics
* inventory file example
```
[staging]
t1   ansible_host=test1.ans

[staging:vars]
ansible_user=root
ansible_ssh_private_key_file=/home/boink/.ssh/id_test1
```
doc: https://docs.ansible.com/ansible/2.7/user_guide/intro_inventory.html  

* config file example
```
[defaults]
host_key_checking = false
inventory         = ./hosts.txt
```
doc: https://docs.ansible.com/ansible/latest/reference_appendices/config.html  

#### ansible info
* check connectivity to host
```
ansible staging -m ping
```

* check os info
```
ansible all -m setup
```  

* check ansible installed module information
```
ansible-doc -l | grep aws*
```  

* get inventory relationships
```
ansible-inventory --list  
ansible-inventory --graph
```

#### ansible actions
* run ad hoc command with and without env
```
ansible all -m shell -a 'hostnamctl' 
ansible all -m command -a 'hostnamctl'
```  

* copy to and remove from multiple hosts
```
ansible all -m copy -a 'src=halo.txt dest=/home mode=777' -b
ansible all -m file -a "path=/home/halo.txt state=absent" -b
```  

* download file from url
```
ansible all -m get_url -a "url=<link> dest=/home" -b
```  

* check uri connectivity on host
```
ansible all -m uri -a "url=https://ya.ru return_content=yes"
```  

* install programs with yum module
```
ansible all -m yum -a "name=tmux state=installed"
```  

* start service
```
ansible all -m service -a "name=httpd state=started"
```  

* create an admin group
```
ansible all -b -m group -a "name=admins state=present"
```

* add user to admin group
```
ansible all -b -m user -a "name=labbrat group=adminz createhome=yes generate_ssh_key=yes"
```

#### ansible extra options
* increase amount (20) of parallel run forks  
```
ansible all -a 'hostname' -f 20
```

* limit connection to a certain host
```
ansible all -b -a "service ntpd restart" --limit "*.4"
```

#### ansible-playbook
* limit playbook to groups and hosts
```
ansible-playbook playbook.yml --limit webservers
ansible-playbook playbook.yml --limit test1.lab
```

* list hosts
```
ansible-playbook playbook.yaml --list-hosts
```

* custom inventory
```
ansible-playbook -i curom_inventory playbook.yaml
```

* run tasks concurrently
```
ansible-playbook init_config.yaml --forks=2
```

* dry run
```
ansible-playbook init_config.yaml --check
```


#### Ansible Navigator
:images ----> show all images
:config ----> shows configuration options

* run playbook
```
ansible-navigator run apache.yml
# output to stdout ----> --mode stdout 
# dry run -------------> --check
```  
