### firewalld
Firewall configuration using `firewall-cmd` in Fedora/AlmaLinux/RedHat type Linux distributions.
**Note** All actions in this readme are for changing live firewalld settings, 
if changes need to be persistent across reboot - add `--permanent` flag

#### Ports
* List ports `firewall-cmd --list-ports`
* Add port `firewall-cmd --add-port=22/tcp`
* Remove port `firewall-cmd --remove-port=22/tcp`
* Reload firewall
  * `firewall-cmd --reload`
  * `systemctl restart firewalld`

#### Restrict SSH to an IP range
```
firewall-cmd --zone=ssh-limited --add-source=192.168.56.0/24
firewall-cmd --zone=ssh-limited --add-service=ssh
firewall-cmd --remove-service=ssh
```

### Useful Links
Fedora `firewalld` documentation: https://docs.fedoraproject.org/en-US/quick-docs/firewalld/
Rich rules: https://www.computernetworkingnotes.com/linux-tutorials/firewalld-rich-rules-explained-with-examples.html
