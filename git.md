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
