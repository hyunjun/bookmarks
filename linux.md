Linux
=====
* [Linux Fundamentals](https://www.youtube.com/playlist?list=PL8A83A276F0D85E70)
* [A little bit about a linux kernel](https://github.com/0xAX/linux-insides)
* [Multitasking in the Linux Kernel. Workqueues](http://kukuruku.co/hub/nix/multitasking-in-the-linux-kernel-workqueues)
* [How to close a running process's socket](http://incoherency.co.uk/blog/stories/closing-a-socket.html)
* [Linuxbrew A fork of Homebrew for Linux](http://brew.sh/linuxbrew/)
* [Why are there both TMP and TEMP environment variables, and which one is right?](http://blogs.msdn.com/b/oldnewthing/archive/2015/04/17/10608077.aspx)
* [Linux Survival](http://linuxsurvival.com/)
* [command line power user](modern command line workflow with ZSH, Z and related tools)
* [Understanding the bin, sbin, usr/bin, usr/sbin Split](http://landley.net/writing/hackermonthly-issue022-pg33.pdf)
* [운영체제 - 이화여자대학교 반효경](http://www.kocw.net/home/search/kemView.do?kemId=1046323&ar=pop)
* [A history of modern init systems (1992-2015)](http://blog.darknedgy.net/technology/2015/09/05/0/)

# Command
* [Learn the Command Line - Learn how to use the command line to manipulate data and automate tasks](https://www.codecademy.com/en/courses/learn-the-command-line)
* [the art of command line - Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
* [No one expect command execution !](http://0x90909090.blogspot.kr/2015/07/no-one-expect-command-execution.html)
* [Explaining Shell Commands in the Shell](https://www.mankier.com/blog/explaining-shell-commands-in-the-shell.html?hn=1)
* [UNIX TOOLBOX](http://cb.vu/unixtoolbox.xhtml)
* [Empty the linux buffer cache](http://www.commandlinefu.com/commands/view/1026/empty-the-linux-buffer-cache) `sync && echo 3 > /proc/sys/vm/drop_caches`
* [More shell, less egg](http://leancrew.com/all-this/2011/12/more-shell-less-egg/) `tr -cs A-Za-z '\n' < [input] | tr A-Z a-z | sort | uniq -c | sort -rn | sed ${1}q`
* [Extract it](http://extractit.mawalabs.de/) command line to extract compressed file
* `awk`
  * sum of numbers in file `awk '{ sum += $1 } END { print sum }' [file name]`
* `comm`
  * `comm -1 -2 [file1] [file2]` print common lines between file1 & file2 (-1 suppresses only lines from file1 & -2 does the same from file2)
    * [reverse diff](http://stackoverflow.com/questions/746458/how-to-show-lines-in-common-reverse-diff)
* crontab
  * [cron and crontab usage and examples](https://www.pantz.org/software/cron/croninfo.html)
* `curl`
  * [A CURL CHEAT SHEET](http://daniel.haxx.se/blog/2015/09/16/a-curl-cheat-sheet/)
  * [online curl commandline builder](https://curlbuilder.com/)
  * [TLS Connection Control](http://blog.mailgun.com/tls-connection-control/)
  * [Use Curl to identify bottlenecks in your service layers](https://gist.github.com/adamkaplan/adf15f0d622f4932f4af)
* `date`
  * `date +%Y%m%d [--date '1 days ago']`
* [dnf - dnf is a package manager based on yum and libsolv](https://github.com/rpm-software-management/dnf)
* `find`
  * `find [directory] -iname "[file name or pattern]" -exec ls -alt {} \;`
  * `find [directory] -name "[file name or pattern]" -exec ls -alt {} \;`
  * `find ~/Downloads/*.pdf -mtime -10` -atime = access / -ctime = creation, file 속성 / -mtime = modification
* `grep`
  * `grep '^[A-Z_]\+[   ]\+[0-9]\+' [file name]` 파일에서 영어 대문자와 _로 시작하고 중간에 스페이스, 탭으로 이뤄진 공백이 있고 숫자로만 끝나는 line 찾기
* `less`
  * [Stop using tail -f (mostly)](http://www.brianstorti.com/stop-using-tail/)
* `mkdir`
  * [get the most out of mkdir](https://blog.hauck.io/get-the-most-out-of-mkdir/)
* [monit](https://mmonit.com/) 설정이 엄청나게 쉽다지만, 간단한 건 upstart가 더 쉬웠음
  * [아마존 웹 서비스 7 – 데몬 자동 부활주문서 monit](http://www.creativeworksofknowledge.com/2015/06/07/aws-daemon-monitoring-using-monit/)
* `mv`
  * [Unix filesystems: How mv can be dangerous](http://jstimpfle.de/fun/mv.html)
* nmap
  * [Nmap Examples For Network Admins](http://teknixx.com/nmap-examples-for-network-admins/)
* [nq - Unix command line queue utility](https://github.com/chneukirchen/nq)
* `objdump` / `gobjdump` (OS X)
  * [example](https://gist.github.com/hyunjun/693e04c3fec40094cef9)
* `pbcopy`
  * [터미널에서 현재 디렉토리를 클립보드로 복사하기](http://www.appilogue.kr/2844595)
* `ping`
  * [The Story of the PING Program](http://ftp.arl.army.mil/~mike/ping.html)
* pipe
  * [Persistent "pipes" in Linux](https://gist.github.com/CAFxX/571a1558db9a7b393579)
* `sed`
  * [Bash Shell: Remove (Trim) White Spaces From String / Variable](http://www.cyberciti.biz/faq/bash-remove-whitespace-from-string/)
    * `sed -e 's/^[ \t]*//'` remove tab & space at the start of the line
    * `sed -e 's/[ \t]*$//'` remove tab & space at the end of the line
  * `sed 's/\xEF\xBB\xBF//g'` remove <feff>
    * [<U+FEFF> character showing up in files. How to remove them?](http://stackoverflow.com/questions/7297888/ufeff-character-showing-up-in-files-how-to-remove-them)
    * [Removing special characters(<200c> <200d> from a text file](http://stackoverflow.com/questions/9257103/removing-special-characters200c-200d-from-a-text-file)
* [seq](http://www.delorie.com/gnu/docs/textutils/coreutils_156.html)
  * `seq -f '%05g' [start number] [end number]` format string %e, %g, %f
* `split`
  * [텍스트 파일을 잘라보자.split](http://darkrang.tistory.com/179)
* `ssh`
  * [Getting Started with SSH](https://semaphoreci.com/community/tutorials/getting-started-with-ssh)
* `strip`
  * [10 Linux Strip Command Examples (Reduce Executable/Binary File Size)](http://www.thegeekstuff.com/2012/09/strip-command-examples/)
* [systemd](http://www.freedesktop.org/wiki/Software/systemd/) redhat 6.3에서는 `configure`가 안 됨
  * [서버 프로세스를 관리하는 올바른 방법](http://www.codeok.net/%EC%84%9C%EB%B2%84%20%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%A5%BC%20%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94%20%EC%98%AC%EB%B0%94%EB%A5%B8%20%EB%B0%A9%EB%B2%95)
  * [How To Install / Upgrade systemd on RHEL/CentOS 7.0](http://linoxide.com/linux-how-to/install-systemd-centos-redhat/)
  * [Why I dislike systemd](http://www.steven-mcdonald.id.au/articles/systemd.shtml)
  * [Systemd is the best example of Suck](http://suckless.org/sucks/systemd)
* `tail`
  * [Stop using tail -f (mostly)](http://www.brianstorti.com/stop-using-tail/)
  * [delete first line of a file](http://unix.stackexchange.com/questions/96226/delete-first-line-of-a-file) `tail -n +2 [file name]`
* `tcpdump`
  * [A gentle introduction to Berkeley Packet Filters](http://tylerfisher.org/bpf/)
* `tr`
  * [remove-all-white-spaces](http://stackoverflow.com/questions/9953448/how-to-remove-all-white-spaces-from-a-given-text-file) `tr -d [:blank:]`
  * [replace-whitespaces-with-tabs-in-linux](http://stackoverflow.com/questions/1424126/replace-whitespaces-with-tabs-in-linux)
* trace
  * [Choosing a Linux Tracer (2015)](http://www.brendangregg.com/blog/2015-07-08/choosing-a-linux-tracer.html)
* [upstart](http://upstart.ubuntu.com/)
  * [The Upstart Event System: What It Is And How To Use It](https://www.digitalocean.com/community/tutorials/the-upstart-event-system-what-it-is-and-how-to-use-it)
  * [RHEL6 SELinux Upstart - How to reload configuration /etc/init/<conf> without a restart?](https://access.redhat.com/discussions/671253)
  * [example](https://gist.github.com/hyunjun/ad60cf79c390b3fe0523)
* `watch`
  * [The watch Command](http://www.linfo.org/watch.html)
  
# CoreOS
* [CoreOS : 설치부터 컨테이너 배포까지](http://www.slideshare.net/subicura/coreos-38279596)
* [Managing CoreOS with Ansible](https://coreos.com/blog/managing-coreos-with-ansible/#inventory-setup)

# Debian
* [AutomaticPackagingTools](https://wiki.debian.org/AutomaticPackagingTools)

# GNU
* [Turn GNU command line tools into SaaS (Stupid Hackathon Project)](https://github.com/diafygi/gnu-pricing)

# Kernel
* [Initialization](https://github.com/0xAX/linux-insides/tree/master/Initialization)
* [The Linux Kernel Module Programming Guide](http://www.tldp.org/LDP/lkmpg/2.6/html/index.html)
* [Kernel bypass](https://blog.cloudflare.com/kernel-bypass/)

## Interrupt
* [Interrupts and Interrupt Handling](https://github.com/0xAX/linux-insides/tree/master/interrupts)

# Library
* [Tutorials and tools for sysadmins and developers](https://syscoding.com/)
* [Colorizing `cat`](https://github.com/jingweno/ccat)
* [fzf-fs - Simple file browsing/navigation with https://github.com/junegunn/fzf](https://github.com/D630/fzf-fs)
* [ix: command line pastebin](http://ix.io/)
* [Lynis - an open source security auditing tool](https://cisofy.com/lynis/)
* [netmap - the fast packet I/O framework](http://info.iet.unipi.it/~luigi/netmap/)
* [NsJail - A light-weight process isolation tool, making use of Linux namespaces and seccomp-bpf](http://google.github.io/nsjail/)
* [Oh-My-Zsh is an open source, community-driven framework for managing your ZSH configuration](http://ohmyz.sh/)
* [pig - A Linux packet crafting tool](https://github.com/rafael-santiago/pig)
* [Qfc - Quick Command-line File Completion](http://pindexis.github.io/qfc/)
* [RTail - Terminal output to the browser in seconds, using UNIX pipes](http://rtail.org/)
* [shed - the sh editor](https://github.com/mplewis/shed)
* [sift is a fast and powerful open source alternative to grep](http://sift-tool.org/info.html)
* [snappy-start: Tool for process startup snapshots](https://github.com/google/snappy-start)
* [spaceman-diff - Diffing Images on the Command Line](http://zachholman.com/posts/command-line-image-diffs/)
* [zindex - Create an index on a compressed text file](https://github.com/mattgodbolt/zindex)

# Memory
* Buffer and Cache
  * Buffer; optimize for block IO. metadata, data stream such as moving Youtube slider. once used, can't use it again.
  * Cache; optimize for disk IO. usually files. use it again and again unless evicted by algorithm such LRU
  * [What is the difference between a cache and a buffer?](http://superuser.com/questions/433948/what-is-the-difference-between-a-cache-and-a-buffer)
  * [Linux memory: buffer vs cache](http://stackoverflow.com/questions/6345020/linux-memory-buffer-vs-cache)
  * [Linux Kernel: What is the major difference between the buffer cache and the page cache?](http://www.quora.com/Linux-Kernel/What-is-the-major-difference-between-the-buffer-cache-and-the-page-cache)
  * [What is the difference between Buffers and Cached columns in /proc/meminfo output?](http://www.quora.com/What-is-the-difference-between-Buffers-and-Cached-columns-in-proc-meminfo-output)
* Stack and Heap
  * [THE STACK AND THE HEAP](https://www.cs.berkeley.edu/~jrs/61b/lec/09) java stack, stack frame, and heap

# Network
* [Beej's Guide to Network Programming Using Internet Sockets](http://beej.us/guide/bgnet/)
  * [html](http://beej.us/guide/bgnet/output/html/multipage/index.html)

# Shell
* [Bash Shortcuts Gem](http://zwischenzugs.tk/index.php/2015/07/01/bash-shortcuts-gem/)
* [Full vim for readline (bash, gdb, python, etc)](https://github.com/ardagnir/athame)
* [Code Inflation](https://www.computer.org/cms/Computer.org/ComputingNow/issues/2015/04/mso2015020010.pdf)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Bash)
* [Share your favourite bash/zsh aliases](https://news.ycombinator.com/item?id=9869231)
* [HyperJump - A Quicker Way to CD](http://sdbr.net/post/HyperJump/)
* [Stronger Shell](http://m.odul.us/blog/2015/8/12/stronger-shell)
* [Beyond Bash - Shell scripting in a typed, OO language](https://docs.google.com/presentation/d/11vZzXCfAA0aOFAuHA0nAvAzALGFGCH-dqHxx6XMgbk8/edit#slide=id.p)
* [Monadic i/o and UNIX shell programming](http://okmij.org/ftp/Computation/monadic-shell.html)

## Library
* [ctypes.sh - A foreign function interface for bash](http://ctypes.sh/)
* [ctypes.sh, a foreign function interface for bash](https://github.com/taviso/ctypes.sh/wiki)
* [Dcron - Job scheduling made easy, distributed and highly-available](http://dcron.io/)
* [Edbrowse, a Command Line Editor Browser](http://edbrowse.org/)
* [Es: a shell with higher-order functions](http://wryun.github.io/es-shell/)
* [fish shell - Finally, a command line shell for the 90s](http://fishshell.com/?version=2.2)
  * [Switching from zsh to fish](http://jbrodriguez.io/switching-from-zsh-to-fish/)
* [journal - A unix/linux command line utility that creates a new journal text file with today's date on your computer](https://github.com/davidkneely/journal)
* [lolcat - Rainbows and unicorns!](https://github.com/busyloop/lolcat)
* [Prezto - Instantly Awesome Zsh](https://github.com/sorin-ionescu/prezto)
* [svsh - Take control of your supervisor](http://ido50.github.io/Svsh/)
* [vnstat - Track and Log a Linux Server's Bandwidth Use](http://www.happyapps.io/blog/2015-08-15-track-and-log-a-linux-server-s-bandwidth-use)

# System Library
* [inotify](http://ko.m.wikipedia.org/wiki/Inotify)
* [로그 (syslog)](http://system-monitoring.readthedocs.org/en/latest/log.html)
* IPC
  * [Beej's Guide to Unix IPC](http://beej.us/guide/bgipc/output/html/multipage/index.html)
  * [Interprocess Communication in the Ninth Edition Unix System](http://cm.bell-labs.co/who/dmr/ipcpaper.html)
* [runit - a UNIX init scheme with service supervision](http://smarden.org/runit/)
* Thread
  * [Raw Linux Threads via System Calls](http://nullprogram.com/blog/2015/05/15/)

# [Tmux](https://tmux.github.io/)
* [install](http://linoxide.com/how-tos/install-tmux-manage-multiple-linux-terminals/)
* [A Tmux crash course: tips and tweaks](http://tangosource.com/blog/a-tmux-crash-course-tips-and-tweaks/)
* [A tmux Crash Course](https://robots.thoughtbot.com/a-tmux-crash-course)
* [tpm - Tmux Plugin Manager](https://github.com/tmux-plugins/tpm)
* [tmux 입문자 시리즈 요약](http://haruair.com/blog/2124)

## troubleshooting
* [tmux protocol version mismatch (client N server M)](http://unix.stackexchange.com/questions/122238/protocol-version-mismatch-client-8-server-6-when-trying-to-upgrade)

  ```
  $ tmux attach
  protocol version mismatch (client 7, server 6)

  $ pgrep tmux
  3429
  $ /proc/3429/exe attach
  ```
