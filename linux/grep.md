### grep

#### general
* `grep -i` -> case insensitive search
* `grep -n` -> show lines where the find occured
* `grep -r` -> find in all files in a directory
* `grep -v` -> find if not present
* `grep -A 3 -B 5` -> show 5 lines before the match and 3 lines after

#### A list of useful grep statements
* `grep -Po '(?<=")[0-9][0-9./]*\.\d+\.\d+\.\d+(?:/\d+)?(?=")'` -> grep quoted IP address, like in firewalld rules
