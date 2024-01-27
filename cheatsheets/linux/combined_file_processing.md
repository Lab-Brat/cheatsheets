### Combined Commands and One-Liners

* `for f in *_prefix_*.epub; do mv "$f" "${f/_prefix_}"; done` -> remove `_prefix_` from all filenames
* `grep 'Host '  ~/.ssh/config | awk '{$1=""; print $0}' | sed 's/^ //'` -> print all Hosts from config file and remove trailing space
* `for i in $(seq 46 -1 36); do history -d $i; done` -> delete history lines 46->36

