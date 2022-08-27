# sed - stremline editor

#### basics
* show contents
```
sed '' sedd.txt
```

* common flags
  * ```i``` ===> change the file
  * ```n``` ===> do not show file contents

* common special characters
  * ```p``` ===> print line
  * ```d``` ===> delete line
  * ```<num>p``` ===> print particular line
  * ```<num>,<num>p``` ===> print range of lines
  * ```<num>~<num>p``` ===> print every other lines

#### adding line
* add 1st line
```
sed '$1i this is line 1' sedd.txt 
```

* add last line
```
sed '$a this is the last line' sedd.txt
```
