### curl
* `curl cheat.sh` -> get content in the console
* `curl -O cheat.sh` -> save content
* `curl -o page_name.html cheat.sh` -> save to specific file

### wget
* `wget cheat.sh` -> download content
* `wget -O file1.txt cheat.sh` -> download to a file
* `wget -r -l 10 -nv -A "repomd.xml" -X "*/Packages" https://repo.distro.org` -> recursively traverse repository tree and download all metadata files
