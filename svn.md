SVN
===

# Command
* [svn (subversion) 사용법](http://seedraker.tistory.com/28)
* add

  ```
  $ svn add src/xdt/apr-1.3.5
  $ svn ci src/xdt/apr-1.3.5 -m "add library files for xtd"
  ```
* blame
* cat
* changelist (cl)
* checkout (co)
  * `svn checkout "http://source.sc.nhncorp.com:21600/svn/ss3/[project_name]" --no-auth-cache`
  * --no-auth-cache; to avoid inputing yes/no
    * [How to remove warning about storing unencrypted password after committing file in svn](http://stackoverflow.com/questions/6606782/how-to-remove-warning-about-storing-unencrypted-password-after-commiting-file-in)
* cleanup
* commit (ci)
  * `svn ci [file name | local path] -m "[message]"`
  * `$ svn ci . -m "to fix bugs"`
* copy (cp)
  * create test branch
    * `svn copy -m "[message]" "[original directory]" "[new directory]"`
    * `$ svn copy -m "test branch for adding people search in movie collection" "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/vs_movie" "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/TRY-vs_movie_add_people_to_movie"`
  * [SVN 사용시에 branch와 merge 잘 이용하기](http://asbear.tistory.com/50)
  * [SVN branch and merge 쉽게 활용하기 #2](http://asbear.tistory.com/72)
* delete (del, remove, rm)

  ```
  svn delete -m "[message]" "[path]"
  $ svn delete -m "delete test directory" "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/branches/TRY-vs_movie_aw"
  svn rm ... --keep-local; undo svn add, not deleting or canceling local modification
  ```
* diff (di)

  ```
  svn diff
  svn diff "[repository 1]" "[repository 2]"
  $ svn diff "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/trunk" "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/branches/TRY-vs_movie_aw"
  $ svn diff 'http://eng/svn/knoa/ext/algo/trunk/' 'http://eng/svn/knoa/ext/algo/branches/demo_111110' > patch_algo
  svn diff [name/url] --revision [num]:[num]
  $ svn diff util.c --revision 201:273
  $ svn diff | grep Index\:
  $ svn diff -r 14368:HEAD http://eng/svn/knoa/ext/algo/branches/demo_111110/ > patch_algo
  $ svn diff -r 14368:HEAD http://eng/svn/knoa/ext/algo/branches/demo_111110/src/main/java/com/knoa/ext/algo/sequence/cg/ConsensusGraphConverter.java
  ```
* export
* help (?, h)
* import

  ```
  svn import -m "[message]" [project name | file name]" "[project url | file url]"
  $ svn import -m "import vs_movie" vs_movie "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie"
  $ svn import -m "[me2day] create trunk" . "http://source.sc.nhncorp.com:21600/svn/ss3/me2day/trunk"
  $ svn import kitchen.0805081158.tar.gz "http://source.sc.nhncorp.com:21600/svn/ss3/kitchen/tags/REL-0805081158.tar.gz" -m "register 0805081158 version(not source, binary archive from admin server)"
  ```
* info
  * `svn info [-R]`
* list (ls)
* lock
* log
* merge
  * commit

    ```
    svn merge -r [rev num to cancel]:[target rev num] [path] ./
    $ svn merge -r 359:356 http://source.sc.nhncorp.com:21600/svn/ss3/kitchen/branches/TRY-kitchen_aw ./
      --- 开捍钦: r359俊辑 r357鳖瘤 '.'俊 开捍钦:
      U    Version.test
      U    link.sh
    $ svn diff | grep Index\:
    $ svn ci . -m "[kitchen] check in the version for auth wizard 1.4.0"
    ```
  * patch -p0 < [patch file name]
    * [patch파일 수동으로 다루기](http://kldp.org/node/108336)
  * merge example

    ```
    $ svn copy http://source.example.com/project/branches/test-source http://source.example.com/project/branches/test-merge -m "[test-merge] to show practice of merging"
    $ svn co http://source.example.com/project/branches/test-merge
    $ cd test-merge
    [test-merge]$ svn merge --dry-run http://source.example.com/project/trunk . 
    [test-merge]$ svn merge http://source.example.com/project/trunk . 
    [test-merge]$ svn resolved ./some/conflict/directory ./some/conflict/file.any
    [test-merge]$ svn revert ./some/conflict/to/remove
    [test-merge]$ svn resolved ./some/conflict/to/remove
    [test-merge]$ svn status
    [test-merge]$ svn ci -m "[test-merge] resolve conflicts"
    [test-merge]$ svn rm http://source.example.com/project/branches/test-merge -m "[test-merge] remove test branch" 
    ```
    * [svn merge with revision not doing what I expect](http://stackoverflow.com/questions/849382/svn-merge-with-revision-not-doing-what-i-expect)
    * [HOW TO RESOLVE SUBVERSION CONFLICTS](http://ariejan.net/2007/07/04/how-to-resolve-subversion-conflicts/)
    * [Deleting an SVN branch](http://stackoverflow.com/questions/3816626/deleting-an-svn-branch)
  * [SVN trunk 변경사항 되돌리기 (SVN Rollback)](http://asbear.tistory.com/74)
* mergeinfo
* mkdir
  * `svn mkdir -m "[message]" "[path]"`
* move (mv, rename, ren)
  * `svn move -m "[message]" "[original path]" "[new path]"`
  * `$ svn move -m "change vs_movie trunk name" "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/trunk" "http://source.sc.nhncorp.com:21600/svn/ss3/vs_movie/vs_movie"`
* propdel (pdel, pd)
* propedit (pedit, pe)
* propget (pget, pg)
* proplist (plist, pl)
* propset (pset, ps)
* resolve
* resolved
* revert
  * `svn revert [path] [-r]   #   checkout 寸矫肺 倒覆, -r篮 recursive`
  * `$ svn revert -R .`
  * [svn: reverting to previous version](http://stackoverflow.com/questions/3807651/svn-reverting-to-previous-version)
  * [Revert or rollback a SVN revision](http://magp.ie/2010/03/25/revert-or-rollback-a-svn-revision/)
* status (stat, st)
* switch (sw)
* unlock
* update (up)

# Error
* Commit Failed. File ... is out of date. ... path not found 

  ```
  svn update
  svn resolved [path]
  svn commit
  ```
  * [How do I correct “Commit Failed. File xxx is out of date. xxx path not found.”](http://stackoverflow.com/questions/819896/how-do-i-correct-commit-failed-file-xxx-is-out-of-date-xxx-path-not-found)
* Cannot commit files which name contains the symbol like @
  * `svn revert 'some@filename@'` append @ at the end of the file name
  * [Why Subversion skips files which contain the @ symbol?](http://stackoverflow.com/questions/1985203/why-subversion-skips-files-which-contain-the-symbol)
