# sed - streamline editor

#### basics
* `sed '' sedd.txt` -> show contents
* common flags
  * `i` -> change the file
  * `n` -> do not show file contents
* common special characters
  * `p` -> print line
  * `d` -> delete line
  * `<num>p` -> print particular line
  * `<num>,<num>p` -> print range of lines
  * `<num>~<num>p` -> print every other lines
* `s/old_word/new_word/` -> substitution structure

#### adding line
* `sed '$1i this is line 1' sedd.txt` -> add 1st line
* `sed '$a this is the last line' sedd.txt` -> add last line

#### substituting words
* `sed 's/1003/XXXXX/' sedd.txt` ->substituting first match in a line  
* `sed 's/1003/XXXXX/g' sedd.txt` -> substituting all matches in a line  
* `sed 's/1003/XXXXX/2' sedd.txt` -> substituting second match in a line 
* `echo /path/to/file | sed 's_path/to_PATH/TO_'` -> substituting with _ delimiter

#### examples
```bash
labbrat@pop-os:~$ cat test_sed.txt 
http://www.example.com/index.html
labbrat@pop-os:~$ 
labbrat@pop-os:~$ sed -i 's/com/org/' test_sed.txt
labbrat@pop-os:~$ cat test_sed.txt 
http://www.example.org/index.html
labbrat@pop-os:~$
labbrat@pop-os:~$ sed 's/^.*org//' test_sed.txt
/index.html
labbrat@pop-os:~$
labbrat@pop-os:~$ sed 's/^.*com/{&}/' test_sed.txt
{http://www.example.com}/index.html
labbrat@pop-os:~$
```
