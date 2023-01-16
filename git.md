### Git

#### Drop changes
```
git rebase -i HEAD~1
#change 'pick' to 'drop'
#if commit was already pushed to repository, then
git add .
git commit -m 'rebase'
git push -f
```


#### Change commit info
```
git rebase -i HEAD~2
#change 'pick' to 'edit'
#change commit author
git commit --amend --author "LabBrat <xoovoox@protonmail.com>" --no-edit
git rebase --continue
git push -f
```


#### Submodules
* initialized submodules `git submodule init`
* update submodules to predefined commit `git submodule update`
* get the latest version of submodules `git submodule update --recursive --remote`


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
