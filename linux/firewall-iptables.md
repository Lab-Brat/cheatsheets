## iptables

#### Listing
There are 2 ways to list all rules:
```
iptables -L
```
List all rules in a better visual way, and:
```
iptables -S
```
which output can be used in scripts to recreate iptables rules.


#### Activate
To activate iptables set the Input to DROP all traffic. 
After disabling all Input traffic, even ping will stop working. 
To reenable it, please do steps from sections below.
```
iptables -P INPUT DROP
```


#### Established and Related
To allow all basic things the Linux server used to do, i.e 
download stuff from repositories, curl webpages etc., 
related and established traffic has to be allowed:
```
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
```


#### Ports
Allow SSH ports
```
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
```
Port can be allowed for a single IP with `-s <ip/subnet_mask>`.


#### Ping
To enable ping again, allow icmp protocol:
```
iptables -A INPUT -p icmp -j ACCEPT
```


#### Blocking Traffic
To block an SSH traffic to a signle IP, or block an interface for that IP:
```
iptables -I INPUT -s 192.168.56.112 -j DROP
iptables -I INPUT -i eth1 -s 192.168.56.112 -j DROP
```
not the `-I` flag instead of `-A`. This is because this rule must go 
before `allow all SSH traffic` rule.


#### Deleting
First get rule IDs, and then specify ID for deletion:
```
iptables -L --line-number
iptables -D INPUT <ID>
```
