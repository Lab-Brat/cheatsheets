### Git

#### Undo changes
```
git rebase -i HEAD~1
#change 'pick' to 'drop'
#if commit was already pushed to repository, then
git add .
git commit -m 'rebase'
git push -f
```

#### Config
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
