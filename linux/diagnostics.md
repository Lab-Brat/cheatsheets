### Linux Systems Diagnostics

#### Disk Usage
* `du -sh *` -> check disk usage of files and dirs
* `du -sh $(ls -A)` -> check disk usage of files and dirs


#### Find
* `find ./ -name "*.log" -exec du -s -h {} \; | sort -h` -> find .log files, show du and sort by size
* `find . -maxdepth 1 -type d -mtime +7 | wc -l` -> find directories older than 7 days

