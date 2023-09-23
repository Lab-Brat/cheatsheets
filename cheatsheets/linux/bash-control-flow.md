

52 changes: 0 additions & 52 deletions 52
cheatsheets/linux/bash-conditions.md
@@ -1,52 +0,0 @@
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
125 changes: 0 additions & 125 deletions 125
cheatsheets/linux/bash-control-flow.md
@@ -1,125 +0,0 @@
### Bash Control Flow

#### if-else
* example: if-else stament with a equality test
```bash
#!/bin/bash

STR_1="Hello"
STR_2="Hello"

if [ $STR_1 = $STR_2 ]
then
    echo "$STR_1 is equal to $STR_2"
else
    echo "$STR_1 is not equal to $STR_2"
fi
```

* example: if-else statement with numeric comparison
```bash
#!/bin/bash

NUM_2=22
NUM_1=44

if [ $NUM_1 -gt $NUM_2 ]
then
    echo "$NUM_1 is greater than $NUM_2"
else
    echo "$NUM_1 is less than $NUM_2"
fi
```


### for
* example: loop through files
```bash
#!/bin/bash

for file in /home/labbrat/github/*
do
    if [ -f $file ]
    then
        echo "$file is a file"
    elif [ -d $file ]
    then
        echo "$file is a directory"
    else
        echo "$file is something else"
    fi
done
```

* example: c style loops
```bash
#!/bin/bash

for (( i = 0; i < 2; i++))
do
    echo "Welcome $i times"
done

for (( a = 1, b = 10; a <= 10; a++, b-- ))
do
    echo "$a - $b"
done
```

* example: nested for loop
```bash
#!/bin/bash

for (( a=0 ; a<=3 ; a++ ))
do
  echo $a

  for (( b=10; b>=5 ; b-- ))
  do
    echo -n "$b->"
  done

  echo ''
done
```

#### while and until
* example: a basic while loop 
```bash
#!/bin/bash

var1=10
while echo $var1
      [ $var1 -gt 0 ]
do
  echo $var1
  var1=$[ $var1 - 1 ]
done
```

* example: a basic until loop
```bash
 #!/bin/bash
 # using the until command

 var1=100

 until [ $var1 -eq 0 ]
 do
    echo $var1
    var1=$[ $var1 - 25 ]
 done
```

* example: looping through csv file contents
```bash
#!/bin/bash

while IFS=',' read -r owner provider ip port
do
    echo "Owner: $owner"
    echo "Provider: $provider"
    echo "IP Address: $ip"
done < ips.csv
```
