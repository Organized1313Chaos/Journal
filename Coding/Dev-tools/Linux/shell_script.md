### Shell Scripting

- It is interpreted not compiled

- `cat /etc/shells`: (get all shells)

- `which bash`: (where is your shell located)

- `touch hello.sh`
(create a new file named hello.sh)

- `ls -al`
list all files with their permissions

- `#! /bin/bash`
(mention the location of uour bash file)

- `echo "hello world"`

- `./hello.sh`

- `chmod +x hello.sh`

- `#This is a comment`

1) system variables (capital)
2) user defined variable


`echo $BASH`
`echo $BASH_VERSION`
`echo $PWD`
`echo $HOME`

`name = Nehul
echo $name`
`
**# variable name should not start with a number**


`READ VARIABLE_NAME`
`echo $VARIABLE_NAME`

`READ name_1 name_2 name_3`

- -p flag to allow input in the same line
- -s silent flag for password
- -a to read an array

- f string type variables are stored in curly braces.

- $REPLY --> default input variable 

- command line variable are accessed like
`$1 $2 $3`
`$0 -- shell script name`

`args = ("$@")`

`$@ -- all the arguments`
`$# -- number of argument passed to the bash script`