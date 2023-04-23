# Infrastructure

#### LDAP
* `ldapsearch -x -h 10.10.10.11 -D "client2@domain.com" -w 'password' -b "cn=Users,dc=<domain>,dc=<com>"` -> search LDAP

#### DNS
* `dig +short <domain-name>` -> query IP address


#### Useful Links
* [(ldapsearch examples)[https://devconnected.com/how-to-search-ldap-using-ldapsearch-examples/]] - ldapsearch examples
