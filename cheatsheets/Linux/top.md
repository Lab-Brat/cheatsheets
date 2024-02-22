### top

#### Basic actions in top
* `H` -> switch to threads view 
* `c` -> show process full path
* `V` -> process tree view
* `u <username>` -> processes run by a particular user
* Sorting output
    * `M` -> sort by memory usage
    * `P` -> sort by CPU usage
    * `N` -> sort by process ID
    * `T` -> sort by the running time
    * `R` -> reverse
* `O` -> Filtering
    * `COMMAND=systemd` -> filter commands that have systemd in the name
    * `!COMMAND=systemd` -> filter commands that don't have systemd in the name
    * `USER=labbrat` -> filter processes started by labbrat user
    * `%CPU>2.0` -> filter processes than have CPU utilization more than 2%
    * `=` -> clear filter
