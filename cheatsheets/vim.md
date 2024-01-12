## VIM
#### insert methods
* i -> insert before a character
* I -> insert in the beggining of line
* a -> insert after a character 
* A -> insert in the end of line
* o -> insert from a new line below
* O -> insert from a new line above

#### Command :
* `:s/word_a/word_b/` -> change word_a to word_b on the selected line
* `:%s/word_a/word_b/g` -> change all word_a occurences to word_b on the whole file
* `set paste` -> set mode to paste, which will not autoindent on paste
* `set nopaste` -> turn of paste mode

#### Combinations 
* add space to multiple lines
```
CTRL+v
select lines
Shift + I
<space>
Esc
```

* add " to the end of multiple lines
```
CTRL+v
select lines
$
Shift + A
"
Esc
```

* indent multiple lines
```
Shift+V
select lines
Shift+.
```
