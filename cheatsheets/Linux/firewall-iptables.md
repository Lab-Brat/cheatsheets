### iptables

#### Listing
There are 2 ways to list all rules:
* `iptables -L` -> list all rules in a better visual way
* `iptables -S` -> which output can be used in scripts to recreate iptables rules


#### Activate
To activate iptables set the Input to DROP all traffic.  
* `iptables -P INPUT DROP` -> drop all input traffic  
**NOTE** After disabling all Input traffic, even ping will stop working.  
To enable ping again, allow icmp protocol:
* `iptables -A INPUT -p icmp -j ACCEPT` -> allow icmp traffic


#### Established and Related
To allow all basic things the Linux server used to do, i.e 
download stuff from repositories, curl webpages etc., 
related and established traffic has to be allowed:
* `iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT` -> allow related and established traffic


#### Ports
Allow SSH ports
* `iptables -A INPUT -p tcp --dport 22 -j ACCEPT` -> allow SSH traffic for incoming traffic
* `iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT` -> allow SSH traffic for outgoing traffic
* `iptables -A INPUT -p tcp --dport 22 -s 192.168.56.112 -j ACCEPT` -> allow SSH traffic for incoming traffic from a single IP


#### Blocking Traffic
* `iptables -I INPUT -s 192.168.56.112 -j DROP` -> drop all traffic from a single IP
* `iptables -I INPUT -i eth1 -s 192.168.56.112 -j DROP` -> drop all traffic from a single IP on a specific interface

**NOTE** `-I` flag is used instead of `-A` because this rule must go before `allow all SSH traffic` rule.


#### Deleting
* `iptables -L --line-number` -> list all rules with line numbers
* `iptables -D INPUT <ID>` -> delete rule with ID


#### Examples
List rules and insert in a specific spot in INPUT chain:
```bash
iptables -t filter -L --line-numbers -n
iptables -I INPUT 1 -i eth1 -d 192.168.66.6 -j ACCEPT
```
