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

#### Undo last * commits
```
# to undo last 1 commit
git reset --hard HEAD~1
git push origin -f
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

#### Switch branch
```
git clone ...
git checkout branch-name

# verify branch switch
git branch 

# to push to that branch
git push origin branch-name
```

#### Pull latest commits from main branch
```
git checkout dev
git fetch origin
git merge origin/main
```

#### Merge changes from dev to main branch
```
git checkout main
git merge dev
git push
```

#### Create and publish tag
```
git tag -a v0.1.1
git push origin v0.1.1
```

#### Submodules
* initialized submodules `git submodule init`
* update submodules to predefined commit `git submodule update`
* get the latest version of submodules `git submodule update --recursive --remote`
