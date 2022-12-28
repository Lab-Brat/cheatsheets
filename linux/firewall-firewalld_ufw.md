### firewalld
Firewall configuration using `firewall-cmd` in Fedora/AlmaLinux/RedHat type Linux distributions.

#### Ports
* List ports `firewall-cmd --list-ports`
* Add port `firewall-cmd --add-port=22/tcp --permanent`
* Remove port `firewall-cmd --remove-port=22/tcp --permanent`
* Reload firewall
  * `firewall-cmd --reload`
  * `systemctl restart firewalld`

#### Restrict SSH to an IP range
```
firewall-cmd --permanent --new-zone=ssh-limited
firewall-cmd --permanent --zone=ssh-limited --add-source=192.168.56.0/24
firewall-cmd --permanent --zone=ssh-limited --add-service=ssh
firewall-cmd --permanent --remove-service=ssh
firewall-cmd --reload
```

### Useful Links
Fedora `firewalld` documentation: https://docs.fedoraproject.org/en-US/quick-docs/firewalld/
Rich rules: https://www.computernetworkingnotes.com/linux-tutorials/firewalld-rich-rules-explained-with-examples.html
