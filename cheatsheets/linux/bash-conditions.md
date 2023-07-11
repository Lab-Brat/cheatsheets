### Bash Conditions

#### numeric comparisons
* `n1 -eq n2` -> Checks if n1 is equal to n2.
* `n1 -ge n2` -> Checks if n1 is greater than or equal to n2.
* `n1 -gt n2` -> Checks if n1 is greater than n2.
* `n1 -le n2` -> Checks if n1 is less than or equal to n2.
* `n1 -lt n2` -> Checks if n1 is less than n2.
* `n1 -ne n2` -> Checks if n1 is not equal to n2.

#### string comparisons
* `str1 = str2` -> Checks if str1 is the same as string str2.
* `str1 != str2` -> Checks if str1 is not the same as str2.
* `str1 \< str2` -> Checks if str1 is less than str2.
* `str1 \> str2` -> Checks if str1 is greater than str2.
* `-n str1` -> Checks if str1 has a length greater than zero.
* `-z str1` -> Checks if str1 has a length of zero.

#### file and directory comparisons
* `-e file` -> Checks if file exists.
* `-d file` -> Checks if file exists and is a directory.
* `-f file` -> Checks if file exists and is a file.
* `-r file` -> Checks if file exists and is readable.
* `-s file` -> Checks if file exists and is not empty.
* `-w file` -> Checks if file exists and is writable.
* `-x file` -> Checks if file exists and is executable.
* `-O file` -> Checks if file exists and is owned by the current user.
* `-G file` -> Checks if file exists and the default group is the same as the current user.
* `file1 -nt file2` -> Checks if file1 is newer than file2.
* `file1 -ot file2` -> Checks if file1 is older than file2.

#### compound test
* `[ condition1 ] && [ condition2 ]` -> AND condition
* `[ condition1 ] || [ condition2 ]` -> OR condition

#### advanced features
* `(command)` -> run command in a subshell
* `(( expression))` -> advance mathematical formula
  * `val ++` -> Post-increment
  * `val --` -> Post-decrement
  * `++ val` -> Pre-increment
  * `-- val` -> Pre-decrement
  * `!` -> Logical negation
  * `~` -> Bitwise negation
  * `**` -> Exponentiation
  * `<<` -> Left bitwise shift
  * `>>` -> Right bitwise shift
  * `&` -> Bitwise Boolean AND
  * `|` -> Bitwise Boolean OR
  * `&&` -> Logical AND
  * `||` -> Logical OR
* `[[ expression ]]` -> pattern matching
