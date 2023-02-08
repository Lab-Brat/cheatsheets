## Portage

#### Basics
* Sync package database `emerge --sync`
* Search for a package `emerge --search <key-word>`
* Install package `emerge --ask <package>`
* Delete package `emerge --deselect <package>`
* Full system upgrade `emerge --update --deep @world`


#### equery
* Install equery `emerge --ask  app-portage/gentoolkit`
* Find all files of a package `equery files <package>`
* Find all docs of a package `equery files --filter=doc <package>`
