### Network Diagnostics Tools

#### mtr
Sends ICMP packets by default
* `mtr <domain>` - default interactive mode
* `mtr -i 0.1 <domain>` - send 10 packets per second
* `mtr -r <domain>` - report mode
* `mtr -T -n <domain>` - send TCP packets and do not resolve DNS

#### traceroute
Sends UDP packages by default

#### tracepath
Sends TCP packages by default

#### netcat
* `nc -v -z <hostname> 80` - connect to port 80 on the remote server
* `nc -v -z localhost 20-30` - connect to local ports 20 - 30 consecutively
