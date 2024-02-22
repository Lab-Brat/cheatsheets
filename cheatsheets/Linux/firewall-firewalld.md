### firewalld
**Note**  
All actions in this cheatsheet are for changing live firewalld settings, 
for changes to be saved after reload add `--permanent` flag

#### Basics
* `firewall-cmd --state` -> Check state 
* `systemctl enable --now firewalld` -> Start firewalld 
* `firewall-cmd --reload` -> Reload firewall
* `systemctl restart firewalld` -> Restart firewall service
* `firewall-cmd --list-all` -> ist default zone rules
* `firewall-cmd --list-all-zones` -> List all zones 
* `firewall-cmd --runtime-to-permanent` -> Save all rules 


#### Ports
* `firewall-cmd --list-ports` -> List ports 
* `firewall-cmd --add-port=22/tcp` -> Add port 
* `firewall-cmd --remove-port=22/tcp` -> Remove port 


#### Services
* `firewall-cnd --add-service=http` -> Add http service 
* `firewall-cmd --remove-service=http` -> Remove service 


#### Restrict SSH to an IP range
* Add source
```
firewall-cmd --zone=public --add-source=192.168.56.0/24
firewall-cmd --zone=public --remove-service=ssh
```

* Add rich-rule
```
firewall-cmd --zone=public --add-rich-rule='rule family=ipv4 source address=192.168.56.0/24 service name=ssh  accept'
firewall-cmd --zone=public --remove-service=ssh
```

### Useful Links
* [[Link]](https://docs.fedoraproject.org/en-US/quick-docs/firewalld/) Fedora `firewalld` documentation
* [[Link]](https://www.computernetworkingnotes.com/linux-tutorials/firewalld-rich-rules-explained-with-examples.html
) Rich rules
