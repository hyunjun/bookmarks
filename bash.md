Shell
=====
* [Bash Koans](https://github.com/marcinbunsch/bash_koans)
* [Full vim for readline (bash, gdb, python, etc)](https://github.com/ardagnir/athame)
* [Code Inflation](https://www.computer.org/cms/Computer.org/ComputingNow/issues/2015/04/mso2015020010.pdf)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Bash)
* [Python Scripts as a Replacement for Bash Utility Scripts](http://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts)
* argument
  * [bash pass multiple arguments with spaces](http://www.linuxquestions.org/questions/linux-software-2/bash-pass-multiple-arguments-with-spaces-717268/)
  * [practice multiple arguments](https://gist.github.com/hyunjun/ba33945e80a4f899cc169f97aa351820)
* array
  * [10.2. Array variables](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_10_02.html)
  * [Bash: convert command line arguments into array](http://stackoverflow.com/questions/12711786/bash-convert-command-line-arguments-into-array)
* stdin
  * [practice - multiple stdin to bash variable](https://gist.github.com/hyunjun/c8aa8398b60b366177385e8dc36d677d#file-multiple_stdin-md)
    * [How to read mutliline input from stdin into variable and how to print one out in shell(sh,bash)?](http://stackoverflow.com/questions/212965/how-to-read-mutliline-input-from-stdin-into-variable-and-how-to-print-one-out-in)
    * [Bash script, read values from stdin pipe](http://stackoverflow.com/questions/2746553/bash-script-read-values-from-stdin-pipe)
* string

  ```
  ${#VAR_NAME} string length
  ${VAR_NAME##*[delimiter]} remove before delimiter
  ${VAR_NAME%[delimiter]*} remove after delimiter
  ```
  * example

    ```
    $ TEST=some_string.ext
    $ echo ${TEST##*_}
    string.ext
    $ echo ${TEST%.*}
    some_string

    $ cat my_script.sh
    THE_DAY_BEFORE_YESTERDAY=`date '+%Y%m%d' --date '2 days ago'`
    YYYYMMDD=${1:-$THE_DAY_BEFORE_YESTERDAY}
    echo $YYYYMMDD
    echo ${YYYYMMDD:6:8}
    echo ${YYYYMMDD::${#YYYYMMDD}-2}
    $ ./my_script.sh
    20170116
    16
    201701
    ```
  * [Advanced Bash-Scripting Guide: Chapter 10. Manipulating Variables](http://tldp.org/LDP/abs/html/string-manipulation.html)
* miscellaneous
  * `CUR_DIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]}))) current directory`
* while
  * [쉡 스크립트 반복문 (while)](http://qnfmfmd.tistory.com/181)

# Library
* [Bash Infinity is a standard library and a boilerplate framework for writing tools using bash](https://github.com/niieani/bash-oo-framework)
* [Sherlock.py - transpiler that translate python to shell script language](https://github.com/Luavis/sherlock.py)
