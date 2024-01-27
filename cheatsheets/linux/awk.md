### awk

#### Basics
* `awk '{print $1, $3}' filename` -> print columns
* `awk '{sum+=$1} END {print sum}' filename` -> sum all columns if they are numbers
* `awk '$1 > 10' filename` -> print lines that matches a certain criteria
* `awk '{$1=""; print $0}'` -> print all but the first column
