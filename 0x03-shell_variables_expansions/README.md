0x03. Shell, init files, variables and expansions
0. a script that creates an alias - alias ls='rm *'
1. a script that prints hello user, where user is the current Linux user - echo hello $USER
2. Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program. - PATH=$PATH:/action
3. a script that counts the number of directories in the PATH - echo $PATH | tr ':' '\n' | wc -l
4. a script that lists environment variables - printenv
5. a script that lists all local variables and environment variables, and functions - set
6. a script that creates a new local variable - BEST="School"
7. a script that creates a new global variable - export BEST="School"
8. a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line - echo $(($TRUEKNOWLEDGE + 128))
9. a script that prints the result of POWER divided by DIVIDE, followed by a new line. - echo $(($POWER/$DIVIDE))
10. a script that displays the result of BREATH to the power LOVE - echo $(($BREATH**$LOVE))
11. a script that converts a number from base 2 to base 10 - echo "$((2#$BINARY))" 
12. a script that prints all possible combinations of two letters, except oo - echo {a..z}{a..z} | tr ' ' '\n' | grep -v 'oo'
13. a script that prints a number with two decimal places, followed by a new line. - printf "%0.2f\n" $NUM
14. a script that converts a number from base 10 to base 16. - printf '%x\n' $DECIMAL
16. a script that encodes and decodes text using the rot13 encryption. Assume ASCII - tr 'A-Za-z' 'N-ZA-Mn-za-m'
17. a script that prints every other line from the input, starting with the first line. - perl -ne 'print if $. % 2 == 1'

