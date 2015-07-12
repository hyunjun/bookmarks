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

# Command
* [the art of command line - Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
* [No one expect command execution !](http://0x90909090.blogspot.kr/2015/07/no-one-expect-command-execution.html)
* crontab
  * [cron and crontab usage and examples](https://www.pantz.org/software/cron/croninfo.html)
* curl
  * [online curl commandline builder](https://curlbuilder.com/)
  * [TLS Connection Control](http://blog.mailgun.com/tls-connection-control/)
* [dnf - dnf is a package manager based on yum and libsolv](https://github.com/rpm-software-management/dnf)
* less
  * [Stop using tail -f (mostly)](http://www.brianstorti.com/stop-using-tail/)
* mkdir
  * [get the most out of mkdir](https://blog.hauck.io/get-the-most-out-of-mkdir/)
* [monit](https://mmonit.com/) 설정이 엄청나게 쉽다지만, 간단한 건 upstart가 더 쉬웠음
  * [아마존 웹 서비스 7 – 데몬 자동 부활주문서 monit](http://www.creativeworksofknowledge.com/2015/06/07/aws-daemon-monitoring-using-monit/)
* mv
  * [Unix filesystems: How mv can be dangerous](http://jstimpfle.de/fun/mv.html)
* nmap
  * [Nmap Examples For Network Admins](http://teknixx.com/nmap-examples-for-network-admins/)
* pbcopy
  * [터미널에서 현재 디렉토리를 클립보드로 복사하기](http://www.appilogue.kr/2844595)
* ping
  * [The Story of the PING Program](http://ftp.arl.army.mil/~mike/ping.html)
* split
  * [텍스트 파일을 잘라보자.split](http://darkrang.tistory.com/179)
* ssh
  * [Getting Started with SSH](https://semaphoreci.com/community/tutorials/getting-started-with-ssh)
* [systemd](http://www.freedesktop.org/wiki/Software/systemd/) redhat 6.3에서는 `configure`가 안 됨
  * [서버 프로세스를 관리하는 올바른 방법](http://www.codeok.net/%EC%84%9C%EB%B2%84%20%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%A5%BC%20%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94%20%EC%98%AC%EB%B0%94%EB%A5%B8%20%EB%B0%A9%EB%B2%95)
  * [How To Install / Upgrade systemd on RHEL/CentOS 7.0](http://linoxide.com/linux-how-to/install-systemd-centos-redhat/)
  * [Why I dislike systemd](http://www.steven-mcdonald.id.au/articles/systemd.shtml)
* tail
  * [Stop using tail -f (mostly)](http://www.brianstorti.com/stop-using-tail/)
* trace
  * [Choosing a Linux Tracer (2015)](http://www.brendangregg.com/blog/2015-07-08/choosing-a-linux-tracer.html)
* [upstart](http://upstart.ubuntu.com/)
  * [The Upstart Event System: What It Is And How To Use It](https://www.digitalocean.com/community/tutorials/the-upstart-event-system-what-it-is-and-how-to-use-it)
  * [RHEL6 SELinux Upstart - How to reload configuration /etc/init/<conf> without a restart?](https://access.redhat.com/discussions/671253)
  * [example](https://gist.github.com/hyunjun/ad60cf79c390b3fe0523)
* watch
  * [The watch Command](http://www.linfo.org/watch.html)
  
# CoreOS
* [CoreOS : 설치부터 컨테이너 배포까지](http://www.slideshare.net/subicura/coreos-38279596)
* [Managing CoreOS with Ansible](https://coreos.com/blog/managing-coreos-with-ansible/#inventory-setup)

# GNU
* [Turn GNU command line tools into SaaS (Stupid Hackathon Project)](https://github.com/diafygi/gnu-pricing)

# Kernel
* [Initialization](https://github.com/0xAX/linux-insides/tree/master/Initialization)

## Interrupt
* [Interrupts and Interrupt Handling](https://github.com/0xAX/linux-insides/tree/master/interrupts)

# Library
* [Tutorials and tools for sysadmins and developers](https://syscoding.com/)
* [Colorizing `cat`](https://github.com/jingweno/ccat)
* [Lynis - an open source security auditing tool](https://cisofy.com/lynis/)
* [NsJail - A light-weight process isolation tool, making use of Linux namespaces and seccomp-bpf](http://google.github.io/nsjail/)
* [Oh-My-Zsh is an open source, community-driven framework for managing your ZSH configuration](http://ohmyz.sh/)
* [shed - the sh editor](https://github.com/mplewis/shed)
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
* [Full vim for readline (bash, gdb, python, etc)](https://github.com/ardagnir/athame)
* [Code Inflation](https://www.computer.org/cms/Computer.org/ComputingNow/issues/2015/04/mso2015020010.pdf)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Bash)
* [Bash Shortcuts Gem](http://zwischenzugs.tk/index.php/2015/07/01/bash-shortcuts-gem/)
* [Share your favourite bash/zsh aliases](https://news.ycombinator.com/item?id=9869231

## Library
* [Prezto - Instantly Awesome Zsh](https://github.com/sorin-ionescu/prezto)
* [Es: a shell with higher-order functions](http://wryun.github.io/es-shell/)
* [fish shell - Finally, a command line shell for the 90s](http://fishshell.com/?version=2.2)
* [lolcat - Rainbows and unicorns!](https://github.com/busyloop/lolcat)

# System Library
* [inotify](http://ko.m.wikipedia.org/wiki/Inotify)
* [로그 (syslog)](http://system-monitoring.readthedocs.org/en/latest/log.html)
* IPC
  * [Beej's Guide to Unix IPC](http://beej.us/guide/bgipc/output/html/multipage/index.html)
  * [Interprocess Communication in the Ninth Edition Unix System](http://cm.bell-labs.co/who/dmr/ipcpaper.html)
* Thread
  * [Raw Linux Threads via System Calls](http://nullprogram.com/blog/2015/05/15/)

# Tmux
* [A Tmux crash course: tips and tweaks](http://tangosource.com/blog/a-tmux-crash-course-tips-and-tweaks/)
* [A tmux Crash Course](https://robots.thoughtbot.com/a-tmux-crash-course)
