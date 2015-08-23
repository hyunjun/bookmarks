Git
===
* [GitHub Engineering](http://githubengineering.com/)
* [git - 간편 안내서](http://rkjun.undefined.kr/git-guide/index.ko.html)
* [생활코딩 - GIT](https://opentutorials.org/course/1492)
* [Git Koans](http://stevelosh.com/blog/2013/04/git-koans/)
* [git-scm.com/book/ko/v1](https://git-scm.com/book/ko/v1/)
* [git-tower.com/learn/git/videos](http://www.git-tower.com/learn/git/videos#episodes)
* [svn 능력자를 위한 git 개념 가이드](http://www.slideshare.net/einsub/svn-git-17386752)
* [핸드스튜디오 사내강의 “Git+, Git 조금 더 배워보기”](http://elegantcoder.com/git-plus/)
* [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-ko.html)
* [How to "Merge" Specific Files from Another Branch](http://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/)
* [Unstage a deleted file in git](http://stackoverflow.com/questions/9591407/unstage-a-deleted-file-in-git)
* [Git Large File Storage](https://git-lfs.github.com/)
  * [Git extension for versioning large files](https://github.com/github/git-lfs)
* [Git in six hundred words](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
* [Git from the inside out](http://maryrosecook.com/blog/post/git-from-the-inside-out)
* [누구나 쉽게 이해할 수 있는 Git 입문](http://backlogtool.com/git-guide/kr/)
* [Deploying branches to GitHub.com](http://githubengineering.com/deploying-branches-to-github-com/)
* [databranches: using git as a database](https://joeyh.name/blog/entry/databranches/)
* [A statistician's initial experiences of Git/GitHub](http://thestatsgeek.com/2015/05/16/a-statisticians-initial-experiences-of-gitgithub/)
* [GitLab flow에서 배울 워크 플로우의 실천](https://translate.google.com/translate?hl=en&sl=ja&tl=ko&u=http%3A%2F%2Fpostd.cc%2Fgitlab-flow%2F)
* [GitFlow considered harmful](http://endoflineblog.com/gitflow-considered-harmful)
* [Unpacking Git packfiles](https://codewords.recurse.com/issues/three/unpacking-git-packfiles/)
* [Scripts to Rule Them All](http://githubengineering.com/scripts-to-rule-them-all/)
* [Towards a production quality open source Git LFS server](https://about.gitlab.com/2015/08/13/towards-a-production-quality-open-source-git-lfs-server/#)
* [Building maintainable step-by-step tutorials with Git](http://info.meteor.com/blog/step-by-step-tutorials-with-git)
* [Git as a Document Format](https://realm.io/news/altconf-wil-shipley-git-document-format/)

# Command
* `add`
  * [Undo 'git add' before commit](http://stackoverflow.com/questions/348170/undo-git-add-before-commit) `git reset <files>`
* `branch`
  * create new branch

    ```
    git branch [new branch]
    ...
    git remote add [new branch]
    git push origin [new branch]
    ```
* `commit`
  * [did you know you can appear to commit as anyone?](https://github.com/amoffat/masquerade)
  * [Blinking Commits](http://blog.annharter.com/2015/08/12/blinking-commits.html)
* [`inject`](https://news.ycombinator.com/item?id=9705690) amend commits other than HEAD
* `log`
  * `git log --oneline --graph --all --branches --decorate`
    * [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit)
    * [Git log in JSON format](https://gist.github.com/varemenos/e95c2e098e657c7688fd)
  * `git log -g --grep=STRING`
    * [How to search for a commit message in github?](http://stackoverflow.com/questions/18122628/how-to-search-for-a-commit-message-in-github)
* undo
  * [How to undo (almost) anything with Git](https://github.com/blog/2019-how-to-undo-almost-anything-with-git)
* pull request
  * [GitHub로 남의 프로젝트에 감놓고 배놓기](https://dogfeet.github.io/articles/2012/how-to-github.html)
  * [example](https://gist.github.com/hyunjun/d61a173e6b81c603ab02)
* `rebase`
  * ['rebaser' improves on 'git rebase -i' by adding information per commit regarding which files it touched](https://gist.github.com/koreno/5893d2d969ccb6b8341d#file-example-L17)

# Library
* [Dockerized gitlab web server http://www.damagehead.com/docker-gitlab/](https://github.com/sameersbn/docker-gitlab)
* [Manage multiple Git identities](https://github.com/prydonius/karn)
* [dns.js.org - free and sleek URL for GitHub Pages](http://dns.js.org/)
* [fugitive](https://github.com/tpope/vim-fugitive)
  * [fugitive-vim-resolving-merge-conflicts-with-vimdiff](http://vimcasts.org/episodes/fugitive-vim-resolving-merge-conflicts-with-vimdiff/)
* [Git Annex](https://git-annex.branchable.com/design/iabackup/)
* [git compound - Compose you projects using Git repositories and Ruby tasks](https://github.com/grzesiek/git_compound/)
* [git-fresh - Fresh Git repository](https://github.com/imsky/git-fresh)
* [gitfs - Version controlled file system](http://www.presslabs.com/gitfs/)
* [Git Miner Dig into guts of git history](https://gitminer.com/)
* [git-hub - Do GitHub operations from the `git` command](https://github.com/ingydotnet/git-hub)
* [Githelp](https://githelp.io/?ref=hackernews)
* [git-meld-index - Run meld or any git difftool to interactively stage changes](https://github.com/jjlee/git-meld-index)
* [Git-mirror-sync - a GitHub service that allows users to easily backup there GitHub repositories to private BitBucket mirrors](http://obihann.github.io/git-mirror-sync/)
* [git-remote-dropbox](http://www.anishathalye.com/2015/08/19/git-remote-dropbox/)
* [GitTorrent: A Decentralized GitHub](http://blog.printf.net/articles/2015/05/29/announcing-gittorrent-a-decentralized-github/)
* [GitUp](http://gitup.co/)
  * [The Git interface you've been missing all your life has finally arrived. http://gitup.co](https://github.com/git-up/GitUp#gitupkit)
* [gitv](https://github.com/gregsexton/gitv)
* [gkv - Git as a KV store](https://github.com/ybur-yug/gkv)
* [Hubaaa's GitHub Vacation Auto-Responder](https://github.com/rbabayoff/hubaaa-github-vacation-responder)
* [hub helps you win at git. http://hub.github.com/](https://github.com/github/hub)
* [pullbox - A dead-simple dropbox alternative using Git](https://github.com/prashanthellina/pullbox)
* [Tig - Text-mode interface for git http://jonas.nitro.dk/tig/](https://github.com/jonas/tig)
  * [Tig: text-mode interface for Git](http://jonas.nitro.dk/tig/)
  * [blogs.atlassian.com/2013/05/git-tig](http://blogs.atlassian.com/2013/05/git-tig/)
* [ungit - The easiest way to use git. On any platform. Anywhere](https://github.com/FredrikNoren/ungit)