Shell
=====
* [Bash Reference Manual](https://tiswww.case.edu/php/chet/bash/bashref.html)
* [Bash 입문자를 위한 핵심 요약 정리 (Shell Script)](https://blog.gaerae.com/2015/01/bash-hello-world.html)
* [Bash shell script 가이드](https://mug896.github.io/bash-shell)
* [Bash Koans](https://github.com/marcinbunsch/bash_koans)
* [Full vim for readline (bash, gdb, python, etc)](https://github.com/ardagnir/athame)
* [Code Inflation](https://www.computer.org/cms/Computer.org/ComputingNow/issues/2015/04/mso2015020010.pdf)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Bash)
* [Python Scripts as a Replacement for Bash Utility Scripts](http://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts)
* [Three Ways to Script Processes in Parallel](https://www.codeword.xyz/2015/09/02/three-ways-to-script-processes-in-parallel/)
* [Sh! Silence your bash scripts by coding your own --silent flag](https://medium.freecodecamp.org/sh-silence-your-bash-scripts-by-coding-your-own-silent-flag-c7e9f8b668a4)
* **[Safe ways to do things in bash](https://github.com/anordal/shellharden/blob/master/how_to_do_things_safely_in_bash.md)**
* [Source code listing for the Lions' Commentary in PDF and PostScript](http://v6.cuzuco.com/)
* [#testing #bash 간단한 assert](http://ohyecloudy.com/pnotes/archives/bash-simple-assert/)
* [Functional and flexible shell scripting tricks](https://medium.freecodecamp.org/functional-and-flexible-shell-scripting-tricks-a2d693be2dd4)
* [bash : 기초 : 셸의 역사, 종류](https://sunyzero.tistory.com/264) profile 참고
* argument
  * [practice - multiple arguments](https://gist.github.com/hyunjun/ba33945e80a4f899cc169f97aa351820)
  * [bash pass multiple arguments with spaces](http://www.linuxquestions.org/questions/linux-software-2/bash-pass-multiple-arguments-with-spaces-717268/)
  * [bash 에서 인자 처리 하기](http://forum.falinux.com/zbxe/?mid=lecture_tip&page=2&document_srl=549896)
* array
  * [practice](https://gist.github.com/hyunjun/ba33945e80a4f899cc169f97aa351820#file-array-sh)
  * [10.2. Array variables](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_10_02.html)
  * [Bash: convert command line arguments into array](http://stackoverflow.com/questions/12711786/bash-convert-command-line-arguments-into-array)
* dictionary, hash table
  * [How to define hash tables in Bash?](https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash)
* expr
  * [Performing Math calculation in Bash](https://www.shell-tips.com/2010/06/14/performing-math-calculation-in-bash/)
* quote
  * [쉘에서 따옴표 안에 같은 종류의 따옴표 넣기](https://hyeonseok.com/soojung/dev/2017/07/16/821.html)
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
  * [practice - split by tab](https://gist.github.com/hyunjun/c8aa8398b60b366177385e8dc36d677d#file-split_by_tab-md)
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
  * `if [[ $string = *"My long"* ]]; then` [String contains in Bash](https://stackoverflow.com/questions/229551/string-contains-in-bash)
  * [uppercase first character in a variable with bash](https://stackoverflow.com/questions/12487424/uppercase-first-character-in-a-variable-with-bash)
    * `${foo^}` capitalize
    * `${foo^^}` uppercase all the letters
    * `${foo,}` lowercase only the first letter
    * `${foo,,}` lowercase all the letters
  * `[ -z "$var" ] && ... || ... ` [Test for non-zero length string in Bash](https://stackoverflow.com/a/3870055)
* miscellaneous
  * `CUR_DIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]}))) current directory`
* while
  * [쉡 스크립트 반복문 (while)](http://qnfmfmd.tistory.com/181)

# Library
* [Bash Infinity - a standard library and a boilerplate framework for writing tools using bash](https://github.com/niieani/bash-oo-framework)
* [bashttpd - a simple, configurable web server written in bash](https://github.com/avleen/bashttpd)
* [ShellCheck finds bugs in your shell scripts](https://www.shellcheck.net/)
  * [쉘 스크립트를 만드는 당신, ShellCheck을 써라!](http://blog.weirdx.io/post/43810/amp)
* [Sherlock.py - transpiler that translate python to shell script language](https://github.com/Luavis/sherlock.py)
