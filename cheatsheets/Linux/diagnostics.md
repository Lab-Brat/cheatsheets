### Linux Systems Diagnostics

#### Disk Usage
* `du -sh *` -> check disk usage of files and dirs
* `du -sh $(ls -A)` -> check disk usage of files and dirs
* `du -ch --max-depth=0 $(ls -d .*) | tail -n 1` -> check disk usage of hidden files and dirs
* `ls -lSrh` -> list files by increasing size

#### Find
* `find ./ -name "*.log" -exec du -s -h {} \; | sort -h` -> find .log files, show du and sort by size
* `find ./ -type f | wc -l` -> count all files in a directory
* `find . -maxdepth 1 -type d -mtime +7 | wc -l` -> find directories older than 7 days
* `find ./ -type f -name "dump.*" -mtime +10 -print0 | du -hc --files0-from - | tail -n 1` -> find dump files older than 10 days and print their combined size
* `find ./ -type f -name "dump.*" -mtime +10 -exec rm -f {} +` -> find files older than 10 days and delete them.
* `find . -name "*.json" ! -path "./build/*" ! -path "./functions/node_modules/*"` -> exclude some paths from find

#### Compare
* `comm -12 <(ls dir1) <(ls dir2)` -> find common files in 2 directories
