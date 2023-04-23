### Systemd Journal
Configuration
* `/etc/systemd/journald.conf` -> main configuration file (should **NOT** be edited)
* `/etc/systemd/journald.conf.d` -> custom configuration files directory  
**# Note**: main configuration file contains every possible option (commented out), which can be used in custom configs as long as they have `.conf` extension.  
**# Note**: with the FSS option it's possible to forbid log alteration without a cryptographic key.

Configuration example, create custom config folder and switch journald to use persisten storage
```bash
mkdir /etc/systemd/journald.conf.d/
cat << END > /etc/systemd/journald.conf.d/storage.conf
[Journal]
Storage=persistent
END
systemctl restart systemd-journald
```

Basic commands
* `journalctl --disk-usage` -> show how much space do logs use
* `journalctl --list-boots` -> show all system boots
* `journalctl -u ssh` -> view logs of one process
* `journalctl -b 0` -> view only the logs of current boot
* `journalctl -f` -> view logs as they arrive
* `journalctl -n 10 /usr/bin/sshd` -> view 10 lines of a process log
* `journalctl --since=yesterday --until=now` -> set time constraint on the log view


### rsyslog
Configuration
* `/etc/rsyslog.conf` -> main configuration file
* `/etc/rsyslog.d/` -> additional configuration files
