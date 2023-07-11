### Random small things in Linux

#### Files and configs
* `readlink -f file.txt` -> get full path of file
* `cat file.txt | xclip -sel clip` -> copy to clipboard
* customize bash promt
```
echo $PS1
vim ~/.bashrc
# change variable ---> PS1='[\u: \W]\$ --> '
```

* add to path
```
echo 'export var=/path/to/script' >> ~/.bashrc
echo 'export PATH=$PATH:$var' >> ~/.bashrc
source ~/.bashrc
```

* check and fix immutable file
```
lsattr /etc/resolv.conf
# immutable output: ----i----------- /etc/resolv.conf
chattr -i /etc/resolv.conf
```

* add desktop icon
```
vim /usr/share/applications/ovito.destop
# add following to the .desktop file
[Desktop Entry]
Name=Ovito
Exec=/home/labbrat/lammps/ovito/bin/ovito
Icon=/home/labbrat/lammps/ovito/share/ovito/doc/manual/html/_static/ovito.ico
Terminal=False
Type=Application
```

#### Locales
* `apt install adobe-source-han-sans-cn-fonts` -> add Chinese character support in browsers 
* `apt install ibus-pinyin && ibus-daemon` -> add pinyin input method 

#### System
* `echo $XDG_SESSION_TYPE` -> check xorg or wayland
* `sed -i "s/quiet/quiet nomodeset/g" /etc/default/grub` -> add kernel flags to grub
* `lsblk -d -o name,rota` -> get HDD or SSD
* `sysctl -w net.ipv4.ping_group_range="0 1000"` -> ping: socket: Operation not permitted
* find distribution info
```
lsb_release -a 
cat /etc/*-release
uname -a
neofetch
```

* open tmux session
```
tmux ls
tmux attach-session -t 0
```

* create systemd service file with timer
```
<name>.service
[Unit]
Description=<service description>

[Service]
ExecStart=<path/to/script.sh>

<name>.timer
[Unit]
Description=<timer description>
Requires=<name>.service

[Timer]
Unit=<name>.service
OnCalendar=*-*-* 00:00:00

[Install]
WantedBy=multi-user.target
```
