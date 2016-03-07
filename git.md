Git
===
* [installation example](https://gist.github.com/hyunjun/5b3124a6110d5198e8cc)
* [GitHub Engineering](http://githubengineering.com/)
* [git - 간편 안내서](http://rkjun.undefined.kr/git-guide/index.ko.html)
* [생활코딩 - GIT](https://opentutorials.org/course/1492)
* [Git Koans](http://stevelosh.com/blog/2013/04/git-koans/)
* [git-scm.com/book/ko/v1](https://git-scm.com/book/ko/v1/)
* [git-tower.com/learn/git/videos](http://www.git-tower.com/learn/git/videos#episodes)
* [19 Tips For Everyday Git Use](http://www.alexkras.com/19-git-tips-for-everyday-use/)
* [Aha! Moments When Learning Git](http://betterexplained.com/articles/aha-moments-when-learning-git/)
* [svn 능력자를 위한 git 개념 가이드](http://www.slideshare.net/einsub/svn-git-17386752)
* [핸드스튜디오 사내강의 “Git+, Git 조금 더 배워보기”](http://elegantcoder.com/git-plus/)
* [Git, GitHub, SSH 이용한 완벽한 작업흐름](http://code.tutsplus.com/ko/tutorials/the-perfect-workflow-with-git-github-and-ssh--net-19564)
* [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-ko.html)
* [Git 브랜치 배우기](http://pcottle.github.io/learnGitBranching/)
* [How to "Merge" Specific Files from Another Branch](http://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/)
* [Unstage a deleted file in git](http://stackoverflow.com/questions/9591407/unstage-a-deleted-file-in-git)
* [Git Large File Storage](https://git-lfs.github.com/)
  * [Git extension for versioning large files](https://github.com/github/git-lfs)
  * [Git Large File Storage v1.0](https://github.com/blog/2069-git-large-file-storage-v1-0)
* [Git in six hundred words](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
* [Git from the inside out](http://maryrosecook.com/blog/post/git-from-the-inside-out)
* [누구나 쉽게 이해할 수 있는 Git 입문](http://backlogtool.com/git-guide/kr/)
* [Deploying branches to GitHub.com](http://githubengineering.com/deploying-branches-to-github-com/)
* [databranches: using git as a database](https://joeyh.name/blog/entry/databranches/)
* [A statistician's initial experiences of Git/GitHub](http://thestatsgeek.com/2015/05/16/a-statisticians-initial-experiences-of-gitgithub/)
* [GitFlow considered harmful](http://endoflineblog.com/gitflow-considered-harmful)
* [Unpacking Git packfiles](https://codewords.recurse.com/issues/three/unpacking-git-packfiles/)
* [Scripts to Rule Them All](http://githubengineering.com/scripts-to-rule-them-all/)
* [Building maintainable step-by-step tutorials with Git](http://info.meteor.com/blog/step-by-step-tutorials-with-git)
* [Git as a Document Format](https://realm.io/news/altconf-wil-shipley-git-document-format/)
* [GitHub Pages 도메인 네임 설정 하기](http://blog.saltfactory.net/github/setting-domain-name-in-github-pages-via-cname.html)
* [UNIVERSE - Two full days on how to build, collaborate, and deploy great software presented by GitHub](http://githubuniverse.com/)
* [Sublime Text2와 Gist로 깔끔하게 code snippet을 사용해 봅시다](https://medium.com/@cookatrice/sublime-text2%EC%99%80-gist%EB%A1%9C-%EA%B9%94%EB%81%94%ED%95%98%EA%B2%8C-code-snippet%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%B4-%EB%B4%85%EC%8B%9C%EB%8B%A4-2518f23ce606)
* [Git from the bottom up](http://ftp.newartisans.com/pub/git.from.bottom.up.pdf)
* [Source Control Solutions](http://blog.xojo.com/source-control-solutions)
* [How short can Git abbreviate?](http://blog.cuviper.com/2013/11/10/how-short-can-git-abbreviate/)
* [디자이너를위한Git #1/2](http://www.slideshare.net/nemofinder/git-git-hub-53514194)
* [Git Concurrency in GitHub Desktop](http://githubengineering.com/git-concurrency-in-github-desktop/)
* [Visualizing Git Concepts with D3](http://onlywei.github.io/explain-git-with-d3)
* [Syncing a fork](https://help.github.com/articles/syncing-a-fork/)
* [04 Yong Seong Song -애저 웹앱을 사용하여 GIT을 활용한 게임 리소스 관리하기](https://channel9.msdn.com/Events/APAC-Influencer-Hero-2015/Korea-Influencer-Showcase/04-Yong-Seong-Song-Game-Development-by-GIT/)

# Command
* `add`
  * [Undo 'git add' before commit](http://stackoverflow.com/questions/348170/undo-git-add-before-commit) `git reset <files>`
* bisect
  * [The git's guide to git: Bisect](http://rkoutnik.com/articles/The-gits-guide-to-git-Bisect.html)
* `branch`
  * create new branch

    ```
    git branch [new branch]
    ...
    git remote add [new branch] remotes/origin/[new branch]
    git push origin [new branch]
    ```
* `commit`
  * [did you know you can appear to commit as anyone?](https://github.com/amoffat/masquerade)
  * [Blinking Commits](http://blog.annharter.com/2015/08/12/blinking-commits.html)
* `diff`
  * `git --no-pager diff` for long line over 80 columns
    * [git diff handling long lines](http://stackoverflow.com/questions/136178/git-diff-handling-long-lines)
* [`inject`](https://news.ycombinator.com/item?id=9705690) amend commits other than HEAD
* `log`
  * `git log --all -- [deleted path/to/file]` [How to locate a deleted file in the commit history?](http://stackoverflow.com/questions/7203515/how-to-locate-a-deleted-file-in-the-commit-history)
  * `git log --oneline --graph --all --branches --decorate`
    * [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit)
    * [Git log in JSON format](https://gist.github.com/varemenos/e95c2e098e657c7688fd)
  * `git log -g --grep=STRING`
    * [How to search for a commit message in github?](http://stackoverflow.com/questions/18122628/how-to-search-for-a-commit-message-in-github)
  * [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/)
  * [A useful template for commit messages](http://codeinthehole.com/writing/a-useful-template-for-commit-messages/)
* merge
  * dry-run [Is there a git-merge --dry-run option?](http://stackoverflow.com/questions/501407/is-there-a-git-merge-dry-run-option)
* undo
  * [How to undo (almost) anything with Git](https://github.com/blog/2019-how-to-undo-almost-anything-with-git)
* pull request
  * [GitHub로 남의 프로젝트에 감놓고 배놓기](https://dogfeet.github.io/articles/2012/how-to-github.html)
  * [example](https://gist.github.com/hyunjun/d61a173e6b81c603ab02)
  * [Checking Out GitHub Pull Requests Locally](http://blog.scottlowe.org/2015/09/04/checking-out-github-pull-requests-locally/)
  * [Bitbucket Pull Requests](https://www.youtube.com/watch?v=ssDHUyrQ8nI)
* `rebase`
  * ['rebaser' improves on 'git rebase -i' by adding information per commit regarding which files it touched](https://gist.github.com/koreno/5893d2d969ccb6b8341d#file-example-L17)
* reset
  * `git reset --hard ORIG_HEAD`
* tag
  * [How to: Delete a remote Git tag](https://nathanhoad.net/how-to-delete-a-remote-git-tag)

# Library
* [Manage multiple Git identities](https://github.com/prydonius/karn)
* [classroom github - Your course assignments on GitHub](https://classroom.github.com/)
* [CloneGits - A tool to clone all of a user's GitHub repos to the local machine](https://github.com/jsnider3/CloneGits)
* [dns.js.org - free and sleek URL for GitHub Pages](http://dns.js.org/)
* [fugitive](https://github.com/tpope/vim-fugitive)
  * [fugitive-vim-resolving-merge-conflicts-with-vimdiff](http://vimcasts.org/episodes/fugitive-vim-resolving-merge-conflicts-with-vimdiff/)
* [gg - hybrid version control system](http://www-cs-students.stanford.edu/~blynn/gg/)
* [GHFS - GitHub repos in your filesystem!](https://github.com/ImJasonH/ghfs)
* [ghrequest - HTTP client for the GitHub API with cache support to get the most of your rate limit](https://github.com/issuetrackapp/ghrequest)
* [Git Annex](https://git-annex.branchable.com/design/iabackup/)
* [gitcolony - THE NEXT GENERATION OF PULL REQUESTS](https://www.gitcolony.com/)
* [git compound - Compose you projects using Git repositories and Ruby tasks](https://github.com/grzesiek/git_compound/)
* [git fastclone](https://corner.squareup.com/2015/11/fastclone.html)
* [git-fresh - Fresh Git repository](https://github.com/imsky/git-fresh)
* [gitfs - Version controlled file system](http://www.presslabs.com/gitfs/)
* [Githelp](https://githelp.io/?ref=hackernews)
* [git-hub - Do GitHub operations from the `git` command](https://github.com/ingydotnet/git-hub)
* [GitHub Hovercard - Quick user hovercard for GitHub](https://github.com/Justineo/github-hovercard)
* [GitLab](https://www.gitlab.com/)
  * [Dockerized gitlab web server http://www.damagehead.com/docker-gitlab/](https://github.com/sameersbn/docker-gitlab)
  * [GitLab flow에서 배울 워크 플로우의 실천](https://translate.google.com/translate?hl=en&sl=ja&tl=ko&u=http%3A%2F%2Fpostd.cc%2Fgitlab-flow%2F)
  * [Towards a production quality open source Git LFS server](https://about.gitlab.com/2015/08/13/towards-a-production-quality-open-source-git-lfs-server/#)
* [git-meld-index - Run meld or any git difftool to interactively stage changes](https://github.com/jjlee/git-meld-index)
* [Git Miner Dig into guts of git history](https://gitminer.com/)
* [Git-mirror-sync - a GitHub service that allows users to easily backup there GitHub repositories to private BitBucket mirrors](http://obihann.github.io/git-mirror-sync/)
* [git-punish](http://git-punish.io/)
* [git-radar - A heads up display for git](https://github.com/michaeldfallen/git-radar)
* [git-remote-dropbox](http://www.anishathalye.com/2015/08/19/git-remote-dropbox/)
* [gitrob - Reconnaissance tool for GitHub organizations http://michenriksen.com/blog/gitrob-putting-the-open-source-in-osint/](https://github.com/michenriksen/gitrob)
* [GitScraper - Downloads entire Git repositories from publicly accessible .git folders over HTTP](https://github.com/delight-im/PHP-GitScraper)
* [gitswarm](http://www.perforce.com/gitswarm)
* [GitTorrent: A Decentralized GitHub](http://blog.printf.net/articles/2015/05/29/announcing-gittorrent-a-decentralized-github/)
* [GitUp](http://gitup.co/)
  * [The Git interface you've been missing all your life has finally arrived. http://gitup.co](https://github.com/git-up/GitUp#gitupkit)
* [gitv](https://github.com/gregsexton/gitv)
* [git-visualizer](http://veniversum.me/git-visualizer/)
* **[gitxiv - Collaborative Open Computer Science](http://gitxiv.com/)**
* [gkv - Git as a KV store](https://github.com/ybur-yug/gkv)
* [Hubaaa's GitHub Vacation Auto-Responder](https://github.com/rbabayoff/hubaaa-github-vacation-responder)
* [hub helps you win at git. http://hub.github.com/](https://github.com/github/hub)
* [husky prevents bad commit or push using Git hooks](https://github.com/typicode/husky)
* [joe - A .gitignore magician in your command line](https://github.com/karan/joe)
* [Pijul, a next-generation distributed version control system](https://pijul.org/)
* [pullbox - A dead-simple dropbox alternative using Git](https://github.com/prashanthellina/pullbox)
* [scientist - 깃허브, 루비 언어용 리팩토링 도구 출시](http://www.bloter.net/archives/249184)
* [SCM Breeze is a set of shell scripts (for bash and zsh) that enhance your interaction with git](https://github.com/ndbroadbent/scm_breeze)
* [Tig - Text-mode interface for git http://jonas.nitro.dk/tig/](https://github.com/jonas/tig)
  * [Tig: text-mode interface for Git](http://jonas.nitro.dk/tig/)
  * [blogs.atlassian.com/2013/05/git-tig](http://blogs.atlassian.com/2013/05/git-tig/)
* [TinyPress - The best GitHub writing platform](https://tinypress.co/)
* [ungit - The easiest way to use git. On any platform. Anywhere](https://github.com/FredrikNoren/ungit)
