### Manage Processes

#### Basics
* `ps aux` - list all running processes
* `kill -9 <pid>` - terminate process
* `pkill -9 <proc_name>` - terminate procees by name
<br/>

#### Kill SSH sessions
Commands:
* `w`and `who`- show who is logged on
* `tty`- show current users pseudo terminal
* `ps -ft pts/1`: get PID of a pseudo terminal  
* `for pid in $(ps -ef | grep "puppet" | awk '{print $2}'); do kill -9 $pid; done` -> kill all sessions that are opened by puppet

Kill SSH session:
* Find sessions
```console
[vagrant@node0 ~]$ w
06:25:51 up 0 min,  2 users,  load average: 0.22, 0.08, 0.03
USER     TTY        LOGIN@   IDLE   JCPU   PCPU WHAT
vagrant  pts/0     06:25    7.00s  0.01s  0.00s w
vagrant  pts/1     06:25    2.00s  0.00s  0.00s -bash
```
* Get PID
```console
[vagrant@node0 ~]$ ps -ft pts/1
UID          PID    PPID  C STIME TTY          TIME CMD
vagrant      981     980  0 06:25 pts/1    00:00:00 -bash
```
* `kill -9 981` - kill session
