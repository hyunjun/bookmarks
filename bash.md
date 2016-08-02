Shell
=====
* [Full vim for readline (bash, gdb, python, etc)](https://github.com/ardagnir/athame)
* [Code Inflation](https://www.computer.org/cms/Computer.org/ComputingNow/issues/2015/04/mso2015020010.pdf)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Bash)
* [Python Scripts as a Replacement for Bash Utility Scripts](http://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts)
* array
  * [10.2. Array variables](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_10_02.html)
* string

  ```
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
    ```
  * [Advanced Bash-Scripting Guide: Chapter 10. Manipulating Variables](http://tldp.org/LDP/abs/html/string-manipulation.html)
* miscellaneous
  * `CUR_DIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]}))) current directory`

