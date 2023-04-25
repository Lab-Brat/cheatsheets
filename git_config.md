### Git Config

#### 2 Account set-up
Here is a configuration of `git` to manage 2 separate `git` accounts (Github and Gitlab for example). 
3 configuration files will be needed
* `.gitconfig` -> main config
* `.gitconfig-lab` -> configuration for Github account
* `.gitconfig-work` -> configuration for Gitlab account

main config
```ini
[includeIf "gitdir:~/github"]
path = ~/github/.gitconfig-lab

[includeIf "gitdir:~/gitlab/"]
path = ~/gitlab/.gitconfig-work
 
[core]
excludesfile = ~/.gitignore
```  

Github config
```ini
[user]
email = self@gmail.com
name = username

[core]
sshCommand = "ssh -i ~/.ssh/key_self"
```  

Gitlab config
```ini
[user]
email = email@work.com
name = username
 
[core]
sshCommand = "ssh -i ~/.ssh/key_work"
```  
