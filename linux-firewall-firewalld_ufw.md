### firewalld
Firewall configuration using ```firewall-cmd``` in Fedora/AlmaLinux/RedHat type Linux distributions.

Ports
* List ports ```firewall-cmd --list-ports```
* Add port ```firewall-cmd --add-port=22/tcp --permanent```
* Remove port ```firewall-cmd --remove-port=22/tcp --permanent```
* Reload firewall
  * ```firewall-cmd --reload```
  * ```systemctl restart firewalld```
