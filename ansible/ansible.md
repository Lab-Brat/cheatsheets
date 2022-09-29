# Ansible

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
