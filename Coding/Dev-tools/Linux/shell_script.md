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

**IF-ELSE**

```
if [condition {comparison operators + logical_operator } ]
then
    statement_if
elif [condition {comparison operators} ]
then
    statement_else_if
else
    statement_else
fi
```
```
String Comparisons:  
---------------------------------
=  compare if two strings are equal
!=  compare if two strings are not equal
-n  evaluate if string length is greater than zero
-z  evaluate if string length is equal to zero 

Examples: 
[ s1 = s2 ]  (true if s1 same as s2, else false)
[ s1 != s2 ]  (true if s1 not same as s2, else false)
[ s1 ]   (true if s1 is not empty, else false)
[ -n s1 ]   (true if s1 has a length greater then 0, else false)
[ -z s2 ]   (true if s2 has a length of 0, otherwise false)

Number Comparisons: 
------------------------------------
-eq compare if two numbers are equal
-ge compare if one number is greater than or equal to a number
-le  compare if one number is less than or equal to a number
-ne  compare if two numbers are not equal
-gt  compare if one number is greater than another number
-lt  compare if one number is less than another number 

Examples: 
[ n1 -eq n2 ]  (true if n1 same as n2, else false)
[ n1 -ge n2 ]  (true if n1greater then or equal to n2, else false)
[ n1 -le n2 ]  (true if n1 less then or equal to n2, else false)
[ n1 -ne n2 ]  (true if n1 is not same as n2, else false)
[ n1 -gt n2 ]  (true if n1 greater then n2, else false)
[ n1 -lt n2 ]  (true if n1 less then n2, else false)
```

- Default of variable = variable_name,automaically variable_name will be taken as a string.
- simple comparisons need to be performed using double brackets instead of single brackets
- Notice the space after and before the square brackets to avoid jumping into error.

```
echo -e "Enter the file name: \c"
read file_name
```
- -e flag is used to enable the interpretation of \c character
- -c tells the cursor to remain in the same place
- -e flag is used to verify if it is  a regular file or not
- -d flag is used to check if it is a directory
- -r read flag, -w write flag, -x execute permission

**Logical Operators**

***AND Operator*** 

- for using And operator use &&
`if [ "$age" -gt 18] && ["$age" -lt 30 ]`

- The -a option provide an alternative compound condition test.
`if [ "$age" -gt 18 -a "$age" -lt 30 ]`

- if `[[ $condition1 && $condition2 ]] `   # Also works.
`if [[ "$age" -gt 18 && "$age" -lt 30 ]]`


***OR Operator*** 

- for using And operator use ||
`if [ "$age" -gt 18] || ["$age" -lt 30 ]`

- The -o option provide an alternative compound condition test.
`if [ "$age" -gt 18 -o "$age" -lt 30 ]`

- if [[ $condition1 || $condition2 ]]    # Also works.
`if [[ "$age" -gt 18 || "$age" -lt 30 ]]`

**Arithmatic Operations**
- Operations: +, -, *, /, %
```
$(( expression ))
echo "Addition = $(( number_1 + number_2 ))"
echo "Addition = $(expr  $number_1 + $number_2 )"
```
-Use \* instead of * to get the correct result instead of syntax error.



**References:**
- [YouTube](http://www.codebind.com/linux-tutorials/bash-shell-scripting-statement-fi-else-fi-elif-else-fi/)

- [Tutorial Website](http://www.codebind.com/linux-tutorials/bash-shell-scripting-statement-fi-else-fi-elif-else-fi/)