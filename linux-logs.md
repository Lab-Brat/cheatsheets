### Systemd Journal
Configuration
* main configuration file (should **NOT** be edited) ```/etc/systemd/journald.conf```
* custom configuration files can be stored at ```/etc/systemd/journald.conf.d``` directory  
**# Note**: main configuration file contains every possible option (commented out), which can be used in custom configs as long as they have ```.conf``` extension.  
**# Note**: with the FSS option it's possible to forbid log alteration without a cryptographic key.

Configuration example, create custom config folder and switch journald to use persisten storage
```console
root@pop-os:~# mkdir /etc/systemd/journald.conf.d/
root@pop-os:~# cat << END > /etc/systemd/journald.conf.d/storage.conf
[Journal]
Storage=persistent
END
root@pop-os:~# systemctl restart systemd-journald
```

Basic commands
* show how much space do logs use ```journalctl --disk-usage```
* show all system boots ```journalctl --list-boots```
* view logs of one process ```journalctl -u ssh```
* view only the logs of current boot ```journalctl -b 0```
* view logs as they arrive ```journalctl -f```
* view 10 lines of a process log ```journalctl -n 10 /usr/bin/sshd```
* set time constraint on the log view ```journalctl --since=yesterday --until=now```
