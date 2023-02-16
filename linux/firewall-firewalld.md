### firewalld
Firewall configuration using `firewall-cmd` in Fedora/AlmaLinux/RedHat type Linux distributions.  
All actions in this cheatsheet are for changing live firewalld settings, 
for changes to be saved after reload add `--permanent` flag
^^^^**Note**  

#### Basics
* Check state `firewall-cmd --state`
* Start firewalld `systemctl enable --now firewalld`
* Reload firewall
  * `firewall-cmd --reload`
  * `systemctl restart firewalld`
* List public (default) zone `firewall-cmd --list-all`
* List all zones `firewall-cmd --list-all-zones`
* Save all rules `firewall-cmd --runtime-to-permanent`


#### Ports
* List ports `firewall-cmd --list-ports`
* Add port `firewall-cmd --add-port=22/tcp`
* Remove port `firewall-cmd --remove-port=22/tcp`

#### Services
* Add service `firewall-cnd --add-service=httpd`
* Remove service `firewall-cmd --remove-service=https`


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
Fedora `firewalld` documentation: https://docs.fedoraproject.org/en-US/quick-docs/firewalld/
Rich rules: https://www.computernetworkingnotes.com/linux-tutorials/firewalld-rich-rules-explained-with-examples.html
