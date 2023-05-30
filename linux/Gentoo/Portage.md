### Portage

#### Basics
* `emerge --sync` -> Sync package database 
* `emerge --search <key-word>` -> Search for a package 
* `emerge --ask <package>` -> Install package 
* `emerge --deselect <package>` -> Delete package 
* `emerge --update --deep @world` -> Full system upgrade 

#### List packages
* `qlist -I | grep <grep>` -> List currently installed packages

#### equery
* `emerge --ask  app-portage/gentoolkit` -> Install equery
* `equery files <package>` -> Find all files of a package 
* `equery files --filter=doc <package>` -> Find all docs of a package
* `equery keywords <package>` -> List available version of a package in the repository
