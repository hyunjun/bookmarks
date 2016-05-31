Linux
=====
* [Linux Fundamentals](https://www.youtube.com/playlist?list=PL8A83A276F0D85E70)
* [A little bit about a linux kernel](https://github.com/0xAX/linux-insides)
* [Multitasking in the Linux Kernel. Workqueues](http://kukuruku.co/hub/nix/multitasking-in-the-linux-kernel-workqueues)
* [How to close a running process's socket](http://incoherency.co.uk/blog/stories/closing-a-socket.html)
* [Linuxbrew A fork of Homebrew for Linux](http://brew.sh/linuxbrew/)
* [Why are there both TMP and TEMP environment variables, and which one is right?](http://blogs.msdn.com/b/oldnewthing/archive/2015/04/17/10608077.aspx)
* [Linux Survival](http://linuxsurvival.com/)
* [Understanding the bin, sbin, usr/bin, usr/sbin Split](http://landley.net/writing/hackermonthly-issue022-pg33.pdf)
* [운영체제 - 이화여자대학교 반효경](http://www.kocw.net/home/search/kemView.do?kemId=1046323&ar=pop)
* [A history of modern init systems (1992-2015)](http://blog.darknedgy.net/technology/2015/09/05/0/)
* [Timers in the Linux kernel](https://github.com/0xAX/linux-insides/blob/master/Timers/timers-1.md)
* [High Performance Multi-core Networked and Storage Systems for Linux](http://natsys-lab.blogspot.kr/2015/09/fast-memory-pool-allocators-boost-nginx.html)
* [Is it a good idea to show everybody what your server is doing?](http://drunken-security.at/archives/41)
* [Raw graphics output on Linux: Part 1](http://orangejuiceliberationfront.com/raw-graphics-output-on-linux-part-1/)
* [Raw graphics output in Linux: Part 2](http://orangejuiceliberationfront.com/raw-graphics-output-in-linux-part-2/)
* [Troubleshooting High I/O Wait in Linux](http://bencane.com/2012/08/06/troubleshooting-high-io-wait-in-linux/)
* [unix - count of columns in file](http://stackoverflow.com/questions/8629330/unix-count-of-columns-in-file) `head -1 stores.dat | tr '|' '\n' | wc -l`
* [가벼운 리눅스 배포판 모음, 보디(Bodhi), 크런치뱅++, 퍼피리눅스 주분투 최소사양](http://startdownload.tistory.com/114)
* [리눅스 배포판 선택, 고민되시나요? - 여기서 최상의 배포판을 골라 보세요](http://sergeswin.com/1056)
* [UNIX 기본, 명령 그리고 관리](https://docs.com/sunnykwak/1556)
* [All about Linux](https://brunch.co.kr/magazine/linux)
* [Understanding the bin, sbin, usr/bin , usr/sbin split](http://lists.busybox.net/pipermail/busybox/2010-December/074114.html)
* [보안 강화 리눅스(Security-Enhanced Linux)](https://lesstif.gitbooks.io/web-service-hardening/content/selinux.html)

# Bash script
* [Advanced Bash-Scripting Guide: Chapter 10. Manipulating Variables](http://tldp.org/LDP/abs/html/string-manipulation.html)
* [Python Scripts as a Replacement for Bash Utility Scripts](http://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts)

# Book
* [리눅스를 활용한 회사 인프라 구축의 모든 것](https://www.lesstif.com/display/1STB/Home)

# Command
* [commandlinefu.com](www.commandlinefu.com)
* [command line power user - modern command line workflow with ZSH, Z and related tools](http://commandlinepoweruser.com/)
* [Learn the Command Line - Learn how to use the command line to manipulate data and automate tasks](https://www.codecademy.com/en/courses/learn-the-command-line)
* [the art of command line - Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
* [Learn Enough Command Line to Be Dangerous](http://www.learnenough.com/command-line)
* [No one expect command execution !](http://0x90909090.blogspot.kr/2015/07/no-one-expect-command-execution.html)
* [Explaining Shell Commands in the Shell](https://www.mankier.com/blog/explaining-shell-commands-in-the-shell.html?hn=1)
* [UNIX TOOLBOX](http://cb.vu/unixtoolbox.xhtml)
* `sync && echo [1|2|3] > /proc/sys/vm/drop_caches` & `[swapoff|swapon] -a`
  * [Empty the linux buffer cache](http://www.commandlinefu.com/commands/view/1026/empty-the-linux-buffer-cache) 
  * [How do you empty the buffers and cache on a Linux system?](http://unix.stackexchange.com/questions/87908/how-do-you-empty-the-buffers-and-cache-on-a-linux-system)
* [More shell, less egg](http://leancrew.com/all-this/2011/12/more-shell-less-egg/) `tr -cs A-Za-z '\n' < [input] | tr A-Z a-z | sort | uniq -c | sort -rn | sed ${1}q`
* [Extract it](http://extractit.mawalabs.de/) command line to extract compressed file
* [Designing Command Line Experiences](http://neovintage.org/product/design/2015/10/01/designing-command-line-experiences/)
* `awk`
  * `$0` means whole line
  * sum of numbers in file `awk '{ sum += $1 } END { print sum }' [file name]`
* `comm`
  * `comm -1 -2 [file1] [file2]` print common lines between file1 & file2 (-1 suppresses only lines from file1 & -2 does the same from file2)
    * [reverse diff](http://stackoverflow.com/questions/746458/how-to-show-lines-in-common-reverse-diff)
* crontab
  * [cron and crontab usage and examples](https://www.pantz.org/software/cron/croninfo.html)
  * `` `date "+\%Y\%m\%d"` `` [How can I execute `date` inside of a cron tab job?](http://unix.stackexchange.com/questions/29578/how-can-i-execute-date-inside-of-a-cron-tab-job)
  * `LANG=ko_KR.UTF-8` [Python3: UnicodeEncodeError only when run from crontab](http://stackoverflow.com/questions/11735363/python3-unicodeencodeerror-only-when-run-from-crontab)
  * [Cron in production? That is a double edged sword!](https://orchestrate.io/blog/2014/03/31/cron-in-production-that-is-a-double-edged-sword/)
  * [crontab.guru](http://crontab.guru/)
* `curl`
  * [A CURL CHEAT SHEET](http://daniel.haxx.se/blog/2015/09/16/a-curl-cheat-sheet/)
  * [online curl commandline builder](https://curlbuilder.com/)
  * [TLS Connection Control](http://blog.mailgun.com/tls-connection-control/)
  * [Use Curl to identify bottlenecks in your service layers](https://gist.github.com/adamkaplan/adf15f0d622f4932f4af)
  * [Is curl|bash insecure?](https://blog.sandstorm.io/news/2015-09-24-is-curl-bash-insecure-pgp-verified-install.html)
* `date`
  * `date +%Y%m%d [--date '1 days ago']`
* df
  * [디스크가 가득 찼을 때](http://wikibook.co.kr/article/when-the-disk-is-full/)
  * [df와 du의 용량차이 발생과 해결(아무리 지워도 디스크 사용량이 줄어들지 않을때)](http://me2c.blogspot.com/2011/02/df-du.html)
* `diff`
  * [Delta is a command-line utility for text diffs. View split diffs in the browser with syntax highlighting (demo), or in the command-line using the --cli flag](http://delta.octavore.com/)
* [dnf - dnf is a package manager based on yum and libsolv](https://github.com/rpm-software-management/dnf)
* du
  * [df와 du의 용량차이 발생과 해결(아무리 지워도 디스크 사용량이 줄어들지 않을때)](http://me2c.blogspot.com/2011/02/df-du.html)
* `find`
  * `find [directory] -iname "[file name or pattern]" -exec ls -alt {} \;`
  * `find [directory] -name "[file name or pattern]" -exec ls -alt {} \;`
  * `find ~/Downloads/*.pdf -mtime -10` -atime = access / -ctime = creation, file 속성 / -mtime = modification
* `grep`
  * `grep '^[A-Z_]\+[   ]\+[0-9]\+' [file name]` 파일에서 영어 대문자와 _로 시작하고 중간에 스페이스, 탭으로 이뤄진 공백이 있고 숫자로만 끝나는 line 찾기
  * [Capturing Groups From a Grep RegEx](http://stackoverflow.com/questions/1891797/capturing-groups-from-a-grep-regex)
    * `grep -Po 'query=\K[a-zA-Z]{16,}'` log에서 query=...으로 되어 있는 부분에서 16자 이상의 영문자만 찾고 싶은 경우. -P는 perl regular expression, \K는 앞 부분은 결과에서 제외, GNU grep version 2.5 이상
* `less`
  * [Stop using tail -f (mostly)](http://www.brianstorti.com/stop-using-tail/)
* `mkdir`
  * [get the most out of mkdir](https://blog.hauck.io/get-the-most-out-of-mkdir/)
* [monit](https://mmonit.com/) 설정이 엄청나게 쉽다지만, 간단한 건 upstart가 더 쉬웠음
  * [아마존 웹 서비스 7 – 데몬 자동 부활주문서 monit](http://www.creativeworksofknowledge.com/2015/06/07/aws-daemon-monitoring-using-monit/)
* `mv`
  * [Unix filesystems: How mv can be dangerous](http://jstimpfle.de/fun/mv.html)
* nc

  ```
  SERVER$ nc -l [port number] > [file name]
  CLIENT$ nc [server ip] [port number] < [file name]

  SERVER$ nc -l [port number] | tar xvfz -
  CLIENT$ tar cvfpz - [files] | nc [server ip] [port number]
  ```
* nm
  * [How do I list the symbols in a .so file](http://stackoverflow.com/questions/34732/how-do-i-list-the-symbols-in-a-so-file)
* nmap
  * [Nmap Examples For Network Admins](http://teknixx.com/nmap-examples-for-network-admins/)
* [nq - Unix command line queue utility](https://github.com/chneukirchen/nq)
* `objdump` / `gobjdump` (OS X)
  * [example](https://gist.github.com/hyunjun/693e04c3fec40094cef9)
* `pbcopy`
  * [터미널에서 현재 디렉토리를 클립보드로 복사하기](http://www.appilogue.kr/2844595)
* `ping`
  * [The Story of the PING Program](http://ftp.arl.army.mil/~mike/ping.html)
  * [prettyping is a wrapper around the standard ping tool with the objective of making the output prettier, more colorful, more compact, and easier to read](http://denilson.sa.nom.br/prettyping/)
* pipe
  * [Persistent "pipes" in Linux](https://gist.github.com/CAFxX/571a1558db9a7b393579)
* `read`
  * [How to read from file or stdin in bash?](http://stackoverflow.com/questions/6980090/how-to-read-from-file-or-stdin-in-bash)
* `sed`
  * [Bash Shell: Remove (Trim) White Spaces From String / Variable](http://www.cyberciti.biz/faq/bash-remove-whitespace-from-string/)
    * `sed -e 's/^[ \t]*//'` remove tab & space at the start of the line
    * `sed -e 's/[ \t]*$//'` remove tab & space at the end of the line
  * `sed 's/\xEF\xBB\xBF//g'` remove <feff>
    * [<U+FEFF> character showing up in files. How to remove them?](http://stackoverflow.com/questions/7297888/ufeff-character-showing-up-in-files-how-to-remove-them)
    * [Removing special characters(<200c> <200d> from a text file](http://stackoverflow.com/questions/9257103/removing-special-characters200c-200d-from-a-text-file)
  * [Delete specific line number(s) from a text file using sed?](http://stackoverflow.com/questions/2112469/delete-specific-line-numbers-from-a-text-file-using-sed)
* [seq](http://www.delorie.com/gnu/docs/textutils/coreutils_156.html)
  * `seq -f '%05g' [start number] [end number]` format string %e, %g, %f
  * [How To Shuffle and Sample on the Command-Line](http://blog.jpalardy.com/posts/how-to-shuffle-and-sample-on-the-command-line/)
* shuf
  * [How To Shuffle and Sample on the Command-Line](http://blog.jpalardy.com/posts/how-to-shuffle-and-sample-on-the-command-line/)
* `sort`
  * `sort -u -t[delimiter] -k[column num],[column num] [file name]` [remove lines based on duplicates within one column](http://unix.stackexchange.com/questions/171091/remove-lines-based-on-duplicates-within-one-column-without-sort)
  * [Sort Files Like A Master With The Linux Sort Command (Bash)](http://www.skorks.com/2010/05/sort-files-like-a-master-with-the-linux-sort-command-bash/)
* `split`
  * [텍스트 파일을 잘라보자.split](http://darkrang.tistory.com/179)
* `ssh`
  * [Getting Started with SSH](https://semaphoreci.com/community/tutorials/getting-started-with-ssh)
* `ssh-copy-id` `ssh-copy-id -i ~/.ssh/id_rsa.pub id@host`
* `stat`
  * `[ 0 = ``stat --printf="%s" $f`` ] && rm $f` remove file if size is 0
* `strip`
  * [10 Linux Strip Command Examples (Reduce Executable/Binary File Size)](http://www.thegeekstuff.com/2012/09/strip-command-examples/)
* [systemd](http://www.freedesktop.org/wiki/Software/systemd/) redhat 6.3에서는 `configure`가 안 됨
  * [How to install, manage, start and autostart ssh service on RHEL 7 Linux](https://linuxconfig.org/how-to-install-manage-start-and-autostart-ssh-service-on-rhel-7-start)
  * [서버 프로세스를 관리하는 올바른 방법](http://www.codeok.net/%EC%84%9C%EB%B2%84%20%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%A5%BC%20%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94%20%EC%98%AC%EB%B0%94%EB%A5%B8%20%EB%B0%A9%EB%B2%95)
  * [How To Install / Upgrade systemd on RHEL/CentOS 7.0](http://linoxide.com/linux-how-to/install-systemd-centos-redhat/)
  * [Why I dislike systemd](http://www.steven-mcdonald.id.au/articles/systemd.shtml)
  * [Systemd is the best example of Suck](http://suckless.org/sucks/systemd)
  * [hastur is a tool for launching systemd-nspawn containers without need of manual configuration](https://github.com/seletskiy/hastur)
* `tail`
  * [Stop using tail -f (mostly)](http://www.brianstorti.com/stop-using-tail/)
  * [delete first line of a file](http://unix.stackexchange.com/questions/96226/delete-first-line-of-a-file) `tail -n +2 [file name]`
* `tcpdump`
  * [A gentle introduction to Berkeley Packet Filters](http://tylerfisher.org/bpf/)
* `top`
  * [Can You Top This? 15 Practical Linux Top Command Examples](http://www.thegeekstuff.com/2010/01/15-practical-unix-linux-top-command-examples/)
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
* [코어OS, 컨테이너 모니터링 도구 오픈소스로 공개](http://www.bloter.net/archives/243792)

# Debian
* [AutomaticPackagingTools](https://wiki.debian.org/AutomaticPackagingTools)

# GCC
* `yum update -y && yum clean all && yum group install "Development Tools" -y` [CentOS / RHEL 7: Install GCC (C and C++ Compiler) and Development Tools](http://www.cyberciti.biz/faq/centos-rhel-7-redhat-linux-install-gcc-compiler-development-tools/)
* `apt-get update && apt-get install -y build-essential` [How to Install Development Tools on Ubuntu, Debian & LinuxMint](http://tecadmin.net/install-development-tools-on-ubuntu/)

# GNU
* [Turn GNU command line tools into SaaS (Stupid Hackathon Project)](https://github.com/diafygi/gnu-pricing)

# Kernel
* [Initialization](https://github.com/0xAX/linux-insides/tree/master/Initialization)
* [The Linux Kernel Module Programming Guide](http://www.tldp.org/LDP/lkmpg/2.6/html/index.html)
* [Kernel bypass](https://blog.cloudflare.com/kernel-bypass/)
* [Linux kernel development](https://github.com/0xAX/linux-insides/blob/master/Misc/contribute.md)

## Interrupt
* [Interrupts and Interrupt Handling](https://github.com/0xAX/linux-insides/tree/master/interrupts)
* [SIGSEGV as control flow - How the JVM optimizes your null checks](http://jcdav.is/2015/10/06/SIGSEGV-as-control-flow/)

# Library
* [Tutorials and tools for sysadmins and developers](https://syscoding.com/)
* [AGREP - approximate GREP for fast fuzzy string searching](https://github.com/Wikinaut/agrep)
* [Colorizing `cat`](https://github.com/jingweno/ccat)
* [desk - Lightweight workspace manager for the shell](https://github.com/jamesob/desk#--desk)
* [fzf-fs - Simple file browsing/navigation with https://github.com/junegunn/fzf](https://github.com/D630/fzf-fs)
* [ICgrep: The fastest way to search text to find the patterns](http://icgrep.com/)
* [ix: command line pastebin](http://ix.io/)
* [Lightning is a tool designed to allow you to find and open files as fast as physically possible](https://github.com/fouric/lightning-cd)
* [Linuxbrew is a fork of Homebrew, the Mac OS package manager, for Linux](https://github.com/Linuxbrew/brew)
* [Lynis - an open source security auditing tool](https://cisofy.com/lynis/)
* [makeself - Make self-extractable archives on Unix](http://stephanepeter.com/makeself/)
* [netmap - the fast packet I/O framework](http://info.iet.unipi.it/~luigi/netmap/)
* [NsJail - A light-weight process isolation tool, making use of Linux namespaces and seccomp-bpf](http://google.github.io/nsjail/)
* [Oh-My-Zsh is an open source, community-driven framework for managing your ZSH configuration](http://ohmyz.sh/)
* [pig - A Linux packet crafting tool](https://github.com/rafael-santiago/pig)
* [prm - A minimal project manager for the terminal](https://github.com/eivind88/prm)
* [Qfc - Quick Command-line File Completion](http://pindexis.github.io/qfc/)
* [RTail - Terminal output to the browser in seconds, using UNIX pipes](http://rtail.org/)
* [shed - the sh editor](https://github.com/mplewis/shed)
* [sift is a fast and powerful open source alternative to grep](http://sift-tool.org/info.html)
  * [Super Fast and Accurate string distance algorithm: Sift4](http://siderite.blogspot.com/2014/11/super-fast-and-accurate-string-distance.html)
* [snappy-start: Tool for process startup snapshots](https://github.com/google/snappy-start)
* [spaceman-diff - Diffing Images on the Command Line](http://zachholman.com/posts/command-line-image-diffs/)
* [sshync - Auto-sync files or directories over SSH using fs.watch()](https://github.com/mateogianolio/sshync)
* [unetbootin.github.io - create bootable Live USB drives](http://unetbootin.github.io/)
* [zindex - Create an index on a compressed text file](https://github.com/mattgodbolt/zindex)

# Memory
* Buffer and Cache
  * Buffer; optimize for block IO. metadata, data stream such as moving Youtube slider. once used, can't use it again.
  * Cache; optimize for disk IO. usually files. use it again and again unless evicted by algorithm such LRU
  * [What is the difference between a cache and a buffer?](http://superuser.com/questions/433948/what-is-the-difference-between-a-cache-and-a-buffer)
  * [Linux memory: buffer vs cache](http://stackoverflow.com/questions/6345020/linux-memory-buffer-vs-cache)
  * [Linux Kernel: What is the major difference between the buffer cache and the page cache?](http://www.quora.com/Linux-Kernel/What-is-the-major-difference-between-the-buffer-cache-and-the-page-cache)
  * [What is the difference between Buffers and Cached columns in /proc/meminfo output?](http://www.quora.com/What-is-the-difference-between-Buffers-and-Cached-columns-in-proc-meminfo-output)
* [hazelnut is an APACHE licensed library written in Python designed to provide a simple and pythonic way to parse the /proc/meminfo file on LINUX based systems.](https://github.com/mrsmn/hazelnut)
* Stack and Heap
  * [THE STACK AND THE HEAP](https://www.cs.berkeley.edu/~jrs/61b/lec/09) java stack, stack frame, and heap
* [linux 환경에서의 메모리 보호기법을 알아보자(1)](https://bpsecblog.wordpress.com/2016/05/16/%EB%A9%94%EB%AA%A8%EB%A6%AC-%EB%B3%B4%ED%98%B8%EA%B8%B0%EB%B2%95/)

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
* [An Asynchronous Shell Prompt](http://www.anishathalye.com/2015/02/07/an-asynchronous-shell-prompt/)
* [쉘 코드 골프 2회 - PATH 변수 내용이 중복되지 않도록 추가하기](https://rm-rf.work/f/topic/56/%EC%89%98-%EC%BD%94%EB%93%9C-%EA%B3%A8%ED%94%84-2%ED%9A%8C-path-%EB%B3%80%EC%88%98-%EB%82%B4%EC%9A%A9%EC%9D%B4-%EC%A4%91%EB%B3%B5%EB%90%98%EC%A7%80-%EC%95%8A%EB%8F%84%EB%A1%9D-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0/4)

## Library
* [ctypes.sh - A foreign function interface for bash](http://ctypes.sh/)
* [ctypes.sh, a foreign function interface for bash](https://github.com/taviso/ctypes.sh/wiki)
* [Dcron - Job scheduling made easy, distributed and highly-available](http://dcron.io/)
* [Edbrowse, a Command Line Editor Browser](http://edbrowse.org/)
* [Es: a shell with higher-order functions](http://wryun.github.io/es-shell/)
* [fish shell - Finally, a command line shell for the 90s](http://fishshell.com/?version=2.2)
  * [Switching from zsh to fish](http://jbrodriguez.io/switching-from-zsh-to-fish/)
  * [fundle - A minimalist package manager for fish inspired by Vundle](https://github.com/tuvistavie/fundle)
* [journal - A unix/linux command line utility that creates a new journal text file with today's date on your computer](https://github.com/davidkneely/journal)
* [lolcat - Rainbows and unicorns!](https://github.com/busyloop/lolcat)
* [nixar - New shell commandsJoyable equivalents for existent linux commands](http://nixar.work)
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
* [Tmux Chess](http://andreykeske.com/#/en/works/tmux-chess?_k=26hj7y)
* 활성/비활성 pane 배경색 분리

  ```
  set-window-option -g window-style 'bg=#181818'
  set-window-option -g window-active-style 'bg=black'
  ```

## troubleshooting
* [tmux protocol version mismatch (client N server M)](http://unix.stackexchange.com/questions/122238/protocol-version-mismatch-client-8-server-6-when-trying-to-upgrade)

  ```
  $ tmux attach
  protocol version mismatch (client 7, server 6)

  $ pgrep tmux
  3429
  $ /proc/3429/exe attach
  ```

# Ubuntu
* [16.04 설치후 세팅](http://programmingsummaries.tistory.com/389)
* [Ubuntu 패키지 저장소 만들기](http://www.joinc.co.kr/w/man/12/deb)
