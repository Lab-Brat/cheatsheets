#### Config
COnfiguration to work with 2 ```git``` accounts, Github and Gitlab for example. 3 configuration files will be needed - ```.gitconfig```, ```.gitconfig-lab``` and ```.gitconfig-work```.  
main config
```
[includeIf "gitdir:~/github"]
path = ~/github/.gitconfig-lab

[includeIf "gitdir:~/gitlab/"]
path = ~/gitlab/.gitconfig-work
 
[core]
excludesfile = ~/.gitignore
```  
work config
```
[user]
email = email@work.com
name = username
 
[core]
sshCommand = "ssh -i ~/.ssh/key_work"
```  
self config
```
[user]
email = self@gmail.com
name = username

[core]
sshCommand = "ssh -i ~/.ssh/key_self"
```  
