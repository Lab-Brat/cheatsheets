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

