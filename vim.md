## VIM
#### insert methods
    * insert before a character -------> i
    * insert in the beggining of line -> I
    * insert after a character --------> a 
    * insert in the end of line -------> A
    * insert from a new line below ----> o
    * insert from a new line above ----> O

#### Combinations 
* add space to multiple lines
```
CTRL+v
select lines
Shift + I
press 'space'
Press Esc.
```

* indent multiple lines
```
Shift+V
select lines
Shift+.
```

#### install from source
```
yum list installed | grep vim
yum -y remove vim-minimal vim-common vim-enhanced

yum -y groupinstall "Development Tools"
yum -y install ncurses-devel git-core

git clone https://github.com/vim/vim && cd vim

./configure --prefix=/usr --with-features=huge --enable-multibyte --with-python-config-dir=/usr/lib/python2.7/config --enable-pythoninterp=yes

make && make install
```
