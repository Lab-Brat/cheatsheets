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

#### adding and removing lines
* `sed '1 i this is line 1' sedd.txt` -> add 1st line
* `sed 'a this is the last line' sedd.txt` -> add last line
* `sed '819,820d' config.yaml` -> remove lines 819 and 820 in config.yaml
* `sed -i '/word/d file.txt'` -> remove lines that contain word

#### substituting words
* `sed 's/1003/XXXXX/' sedd.txt` -> substituting first match in a line  
* `sed 's/1003/XXXXX/g' sedd.txt` -> substituting all matches in a line  
* `sed 's/1003/XXXXX/2' sedd.txt` -> substituting second match in a line 
* `echo /path/to/file | sed 's_path/to_PATH/TO_'` -> substituting with _ delimiter

#### list of useful sed statements
* `sed -i 's/[[:space:]]*$//' $(find yaml_files/ -type f -name "*.yaml")` -> remove trailing in yaml files
* Working with URL, example - `http://www.example.com/index.html`:
  * `sed -i 's/com/org/' <url>` -> change .com -> .org
  * `sed 's/^.*org//' <url>` -> keep filename, i.e `/index.html`
  * `sed 's/^.*com/{&}/' <url>` -> surround the url with braces, i.e `{http://www.example.com}/index.html`
* `sed 's/\(.*\) \(.*\)/\2 \1/' input_file` -> swap places of the two matches separated by 1 space
