## iptables

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

#### Ping
To enable ping again, allow icmp protocol:
```
iptables -A INPUT -p icmp -j ACCEPT
```
