### grep

#### general
* `grep -i` -> case insensitive search
* `grep -n` -> show lines where the find occured
* `grep -r` -> find in all files in a directory
* `grep -v` -> find if not present
* `grep -A 3 -B 5` -> show 5 lines before the match and 3 lines after
* `grep -l` -> show only filename of the matched file. `-L` is to show unmatched

#### A list of useful grep statements
* `grep -Po '(?<=")[0-9][0-9./]*\.\d+\.\d+\.\d+(?:/\d+)?(?=")'` -> grep quoted IP address, like in firewalld rules
* `sed -i '819,820d' config.yaml` -> remove lines 819 and 820 in config.yaml
* `sed '2 i NEW LINE' config.yaml` -> Insert 'NEW LINE' to line 2 in config.yaml
