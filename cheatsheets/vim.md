## VIM
#### Insert methods
* i -> insert before a character
* I -> insert in the beggining of line
* a -> insert after a character 
* A -> insert in the end of line
* o -> insert from a new line below
* O -> insert from a new line above

#### Move cursor
* 0 -> Move cursor to the beginning
* $ -> Move curson to the end
* `f <space>` -> Move cursor to the next space
* `F <space>` -> Move cursor to the previous space

#### Command :
* `:s/word_a/word_b/` -> change word_a to word_b on the selected line
* `:%s/word_a/word_b/g` -> change all word_a occurences to word_b on the whole file
* `:g/word_a/d` -> delete all lines containing word_a
* `:j` -> join the line the cursor is with the line below
* `:sort` -> sort selected lines
* `:set paste` -> set mode to paste, which will not autoindent on paste
* `:set nopaste` -> turn of paste mode

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

#### Macros
Use a macro to combine 2 lines into a comma separated line in a 100 lines file:
* Go to the begging of the first line
* `q2` -> define macro named 2
* `Shift+v <down arrow> J` -> join 2 lines together with a space
* `r ,` -> replace the space with ,
* `<down arrow 0>` -> move to the line below and move the cursor to the beginning
* `q` -> save macro
* `49 @ 2` -> apply the macro for the rest of the file (100/2 - 1)
