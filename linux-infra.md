# Infrastructure

#### LDAP
* query
```
ldapsearch -x -h 10.10.10.11 -D "client2@domain.com" -w 'password' -b "cn=Users,dc=<domain>,dc=<com>"
```
* ldapsearch examples  
https://devconnected.com/how-to-search-ldap-using-ldapsearch-examples/


#### DNS
* query IP address
```
dig +short <domain-name>
```
