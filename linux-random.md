# Random small things in Linux

#### Files and configs
* get full path of file
```
readlink -f file.txt
```

* copy to clipboard
```
cat file.txt | xclip -sel clip
```

* customize bash promt
```
echo $PS1
vim ~/.bashrc
# change variable ---> PS1='[\u: \W]\$ --> '
```

* add to path
```
vim ~/.bashrc
# add the following
# ---> export var=/path/to/script
# ---> export PATH=$PATH:$var
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
* add Chinese character support in browsers 
```
apt install adobe-source-han-sans-cn-fonts
```

* add pinyin input method 
```
apt install ibus-pinyin
ibus-daemon
```

#### System
* check xorg or wayland
```
echo $XDG_SESSION_TYPE
```

* add kernel flags with grub
```
sed -i "s/quiet/quiet nomodeset/g" /etc/default/grub
```

* find distribution info
```
lsb_release -a 
cat /etc/*-release
uname -a
neofetch
```

* get HDD or SSD
```
lsblk -d -o name,rota
```

* open tmux session
```
tmux ls
tmux attach-session -t 0
```

* ping: socket: Operation not permitted
```
sysctl -w net.ipv4.ping_group_range="0 1000"
```
