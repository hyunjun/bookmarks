Vim
===
* [Vim Koans](https://sanctum.geek.nz/arabesque/vim-koans/)
* [A vim Tutorial and Primer](https://danielmiessler.com/study/vim/)
* [openvim.com](http://www.openvim.com/)
* [hea-www.harvard.edu/~fine/Tech/vi.html](http://hea-www.harvard.edu/~fine/Tech/vi.html)
* buffers
  * [How do I close a single buffer (out of many) in Vim?](http://stackoverflow.com/questions/1269648/how-do-i-close-a-single-buffer-out-of-many-in-vim)
* ctags
  * .vimrc에 `set tags+=/path/to/tags`를 추가 or `:set tags+=path/to/tags`
  * [Ctags 설정 및 사용법](http://sungto.tistory.com/34)
  * [Python을 위한 ctags 세팅](https://rampart81.github.io/2017/python-ctags/)

    ```
    ctags -R --fields=+l --languages=python --python-kinds=-iv -f ./tags . $(python -c "import os, sys; print(' '.join('{}'.format(d) for d in sys.path if os.path.isdir(d)))")
    alias python_ctags="ctags -R --fields=+l --languages=python --python-kinds=-iv -f ./tags . $(python -c "import os, sys; print(' '.join('{}'.format(d) for d in sys.path if os.path.isdir(d)))")"
    ```
* quickfix
  * [vim quickfix 기능 - 컴파일 에러 수정](http://sunyzero.tistory.com/223)
* replace
  * [Search_and_replace_in_multiple_buffers](http://vim.wikia.com/wiki/Search_and_replace_in_multiple_buffers)
  * example; remove all the spaces at the end of string

    ```
    :arg *.c
    :argadd *.h
    :argdo %s/[ ]\+$//ge | update
    ```
  * `ggVGu` change all the letters to lowercase [How to convert all text to lowercase in Vim](https://stackoverflow.com/questions/1102859/how-to-convert-all-text-to-lowercase-in-vim)
* [sort](http://vim.wikia.com/wiki/Sort_lines)
  * `:sort` / `:sort!` / `:%!sort -k2nr`
  * [Sorting columns of text in Vim using sort](https://jordanelver.co.uk/blog/2014/03/12/sorting-columnds-of-text-in-vim-using-sort/)
* splits
  * horizontal splits `ctrl + w + J` <-> vertical splits `ctrl + w + H`
* vimdiff
  * [vimdiff cheat sheet](https://gist.github.com/mattratleph/4026987)
  * [Quick and Dirty : Vimdiff Tutorial](http://amjith.blogspot.com/2008/08/quick-and-dirty-vimdiff-tutorial.html)
  * [EnhancedDiff plugin](https://github.com/chrisbra/vim-diff-enhanced)
* vimgrep
  * `:vimgrep [string to find] [target file]`
    * e.g. `:vimgrep /<emphasis>vim<\/emphasis>/ *.xml`
  * [jump command](http://stackoverflow.com/questions/7880372/how-to-jump-between-patterns-when-using-vimgrep-quickfix-list)
    * `:cn`, `:cp` jump to the next and previous entry
    * `:cnf`, `:cpf` jump to the next and previous file
    * `:cr`, `:cla` go to the beginning and end of the quickfix list
    * `:col`, `:cnew` iterate through historical quickfix lists
* vimrc
  * [vimrc.io](http://vimrc.io/)
  * [Vim 사용자 정의 파일 타입 꾸미기](http://www.popit.kr/adding-custom-file-type-in-vim/) for syntax highlight
  * [vimrc-vundle-script](https://github.com/uyu423/vimrc-vundle-script/blob/master/README.md) 여러 리눅스 환경에서의 vimrc, vim plugin 파일 동기화를 위한 저장소
* [빔 편집기 한글화](http://vim-ko.github.io/)
* [Vim cheat sheet](http://csnipp.com/s/69/-Vim-Cheat-Sheet)
* [100 Vim commands every programmer should know](http://www.catswhocode.com/blog/100-vim-commands-every-programmer-should-know)
* [Vim Genius](http://www.vimgenius.com/)
* [vimcasts.org](http://vimcasts.org/)
* [How to boost your Vim productivity](http://sheerun.net/2014/03/21/how-to-boost-your-vim-productivity/)
* [VIM: 8 Takeaways From One Year Of Typing](http://sankho.github.io/web_log/2015/08/02/vim-8-takeaways-from-one-year-of-typing.html)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Vim)
* [neovim](http://neovim.io/)
  * `~/.config/nvim/init.vim` [default location of configuration file](https://github.com/neovim/neovim/wiki/FAQ) just copy .vimrc as init.vim
  * [neovim-dot-app - Mac OS X GUI for Neovim](https://github.com/rogual/neovim-dot-app)
  * [Oceanic Next theme for neovim](https://github.com/mhartington/oceanic-next)
  * [Vim-fork focused on extensibility and agility. Consider helping sustain Neovim development! https://salt.bountysource.com/teams/neovim](https://github.com/neovim/neovim)
  * [example of init.vim](https://gist.github.com/synasius/5cdc75c1c8171732c817)
  * [A guide to neovim](http://nerditya.com/code/guide-to-neovim/)
* [vim plugin to interact with tmux](https://github.com/benmills/vimux)
* **[What are the most amazing things that can be done with Vim?](https://www.quora.com/What-are-the-most-amazing-things-that-can-be-done-with-Vim)**
* [Use Vim everywhere you've always wanted to](https://github.com/cknadler/vim-anywhere)
* [History Is a Tree](http://ideasintosoftware.com/history-is-a-tree/)
* [You have decided to use vi as your main text editor. A few tricks that will help you improve your skills](https://david.padilla.cc/posts/12-you-have-decided-to-use-vi-as-your-main-text-editor-a-few-tricks-to-improve-your-skills)
* [Auto-Reload Your Vimrc](http://www.bestofvim.com/tip/auto-reload-your-vimrc/)
* [Vim Tips For Intermediate Users](http://ideasintosoftware.com/vim-productivity-tips/) relative line numbers, saving on focus lost, and vertical buffers
* [Best of Vim Tips](http://zzapper.co.uk/vimtips.html)
* [Vim speed is not really the point](https://wrongsideofmemphis.wordpress.com/2013/03/27/vim-speed-is-not-really-the-point/)
* [Scala development in Vim](https://advancedweb.hu/2015/06/11/vim-scala/)
* [From TextMate to Vim](http://pchm.co/from-textmate-to-vim/)
* [vimcolors](http://vimcolors.com/)
* [colour schemes - Colour schemes for a variety of editors created by Dayle Rees. http://daylerees.github.io](https://github.com/daylerees/colour-schemes)
  * [daylerees.github.io](http://daylerees.github.io/)
* [Vim's 400 line function to wait for keyboard input](http://geoff.greer.fm/vim/#realwaitforchar)
* [HN Vimmy Bot](http://hnvimmybot.com/)
* [How I Write Invoices in Vim](http://jezenthomas.com/how-i-write-invoices-in-vim/)
* [VIM SETUP FOR MARKDOWN](http://www.swamphogg.com/2015/vim-setup/)
* [Vim Creep](http://www.norfolkwinters.com/vim-creep/)
* [A Simpler Vim Statusline](http://www.blaenkdenum.com/posts/a-simpler-vim-statusline/)
* [Vim and Composability](http://ferd.ca/vim-and-composability.html)
* [Vim: convenient code navigation for your projects](http://dmitryfrank.com/articles/vim_project_code_navigation)
* [How do I edit current shell command in VI](http://apple.stackexchange.com/questions/88515/how-do-i-edit-current-shell-command-in-vi
  * `set -o vi` - `esc` - `v`
* [What's your best Vim related shell script?](https://www.reddit.com/r/vim/comments/3oo156/whats_your_best_vim_related_shell_script/)
* [Entering special characters](http://vim.wikia.com/wiki/Entering_special_characters)
* [Highlight current line](http://vim.wikia.com/wiki/Highlight_current_line)
* [VIM adventures](http://vim-adventures.com/)
* [Vim에서 shell 사용하기](https://www.youtube.com/watch?v=_LJNar5tDfY&feature=youtu.be)
* [<U+FEFF> character showing up in files. How to remove them?](http://stackoverflow.com/questions/7297888/ufeff-character-showing-up-in-files-how-to-remove-them) `:s/[\uFEFF]//g`
* [How to remove this symbol “^@” with vim?](http://superuser.com/questions/75130/how-to-remove-this-symbol-with-vim) `%s/<CTRL-2>//g` `%s/<CTRL-SHIFT-2>//g` (on Mac)
* **[vimgifs.com](http://vimgifs.com)**
* [Your problem with Vim is that you don't grok vi](http://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim/1220118#1220118)
* [Vim anti-patterns](https://sanctum.geek.nz/arabesque/vim-anti-patterns/)
* [exercise-2. vi를 효과적으로 연습하는 방법](https://www.youtube.com/watch?v=_dZk_jv5WlQ)
* [How to Do 90% of What Plugins Do (With Just Vim)](https://youtu.be/XA2WjJbmmoM)
  * ["Slides" and supplemental info from my August 3rd 2016 NYC Vim talk](https://github.com/mcantor/no_plugins)
  * [reddit/how_to_do_90_of_what_plugins_do_with_just_vim](https://www.reddit.com/r/vim/comments/5607lj/how_to_do_90_of_what_plugins_do_with_just_vim/)
* [cheatsheets/vimscript.html](http://ricostacruz.com/cheatsheets/vimscript.html)
* [vim + tmux - OMG!Code](https://www.youtube.com/watch?v=5r6yzFEXajQ)
  * [Vim workshop](https://github.com/nicknisi/vim-workshop)
* [Vim with Windows | 한상곤 Sangkon Han | 2016.07](https://www.youtube.com/watch?v=pKrrw-mfzHg)
* [vi를 진정으로 이해해라](https://blog.weirdx.io/post/39518)
* [The Past and Future of Vim-go](https://speakerdeck.com/farslan/the-past-and-future-of-vim-go)
* [Creating Your Lovely Color Scheme](https://speakerdeck.com/cocopon/creating-your-lovely-color-scheme)
* [Vim, Me and Community](https://docs.google.com/presentation/d/14pViuMI_X_PiNwQD8nuGRG72GUqSeKDqoJqjAZWS39U/view#slide=id.p)
* [Why I love Vim: It’s the lesser-known features that make it so amazing](https://medium.freecodecamp.org/learn-linux-vim-basic-features-19134461ab85)
* [모든 앱에서 Vim을 사용하는 법 - QuickCursorKM과 vim-anywhere](https://nolboo.kim/blog/2018/02/17/vim-anywhere/)

# Library
* [Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile. https://powerline.readthedocs.org/en/latest/](https://github.com/powerline/powerline)
* [vim-airline](https://github.com/vim-airline) lean & mean status/tabline for vim that's light as air
* [Vim Bootstrap - A generator which provides a simple method of generating a .vimrc configuration for vim](http://www.vim-bootstrap.com/)
* [vim-galore - Everything you need to know about Vim](https://github.com/mhinz/vim-galore/)
* [vimwiki - A Personal Wiki For Vim](https://github.com/vimwiki/vimwiki)
  * [Vimwiki + Jekyll + Github.io로 나만의 위키를 만들자](https://johngrib.github.io/blog/2017/12/06/my-wiki/)

# Plugin
* [Python으로 vim plugin 만들기](http://www.slideshare.net/mysqlguru/python-vim-plugin)
* [레거시 코드를 파괴하는 Vim 벽돌 깨기](http://woowabros.github.io/tools/2017/07/06/vim-game-code-break.html)
* [anderson.vim - Dark vim colorscheme based on colors from Wes Anderson films](https://github.com/gilgigilgil/anderson.vim)
* autosave
  * [Vim에서 저장하는 방법 - 자동 저장](https://nolboo.kim/blog/2017/09/14/vim-write-autosave/)
* [diminactive.vim This is a plugin for Vim to dim inactive windows](https://github.com/blueyed/vim-diminactive)
* [Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [Plugin completion using VimAwesome API](https://gist.github.com/junegunn/5dff641d68d20ba309ce)
* [Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile. https://powerline.readthedocs.org/en/latest/](https://github.com/powerline/powerline)
* [Snake - Full Python Scripting in Vim](https://github.com/amoffat/snake)
* [vim-flake8](https://github.com/nvie/vim-flake8)
* [vim-github-dashboard - 그래, 가끔 "Vim에서" GitHub을 보자!](http://tech.kakao.com/2016/03/03/vim-github-dashboard/)
* [vim-go - Go development plugin for Vim](https://github.com/fatih/vim-go)
  * [Go Development with Vim-go](https://www.youtube.com/watch?v=7BqJ8dzygtU)
* [vim-pathogen](https://github.com/tpope/vim-pathogen)
* [vim-plug - Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [vim-python-mode](https://github.com/klen/python-mode)
* [vim scripts](http://vim-scripts.org/vim/scripts.html)
* [Vundle](https://github.com/VundleVim/Vundle.vim)
  * [vim 사용자를 위한 플러그인 매니저 vundle 을 소개 합니다](https://kldp.org/node/125263?destination=node%2F125263)
  * [vundle + vim-flake8 install example](https://gist.github.com/hyunjun/f4103247e247bc802b90)
  * go

    ```
    $ [https_proxy=http://x.y.z:port] git clone https://github.com/fatih/vim-go.git ~/.vim/bundle/vim-go
    $ [http_proxy=http://x.y.z:port https_proxy=http://x.y.z:port] vi ~/.vimrc
    ...
    call vundle#begin()
    ...
    Plugin 'faith/vim-go'
    ...
    call vundle#end()
    :w
    :PluginInstall
    ```
  * [vim-scala](https://github.com/derekwyatt/vim-scala)

    ```
    $ mkdir -p ~/.vim/{ftdetect,indent,syntax} && for d in ftdetect indent syntax ; do https_proxy=http://x.y.z:port curl -o ~/.vim/$d/scala.vim https://raw.githubusercontent.com/derekwyatt/vim-scala/master/$d/scala.vim; done
    $ [http_proxy=http://x.y.z:port https_proxy=http://x.y.z:port] vi ~/.vimrc
    ...
    call vundle#begin()
    ...
    Plugin 'derekwyatt/vim-scala'
    ...
    call vundle#end()
    :w
    :PluginInstall
    ```
* [IntelliJ 의 VIM 플러그인 마개조하기](http://woowabros.github.io/tools/2016/06/18/ideavim-customize-00.html)
* [Vi를 좋아하시는 분들을 위하여](http://greatkim91.tistory.com/m/196)

# Vim8
* vim8의 비동기 기능(job/channel)을 사용한 플러그인들
  * [agrep](https://github.com/ramele/agrep) Asynchronous grep plugin for Vim
  * [ale](https://github.com/w0rp/ale) Asynchronous Lint Engine
  * [asyncrun.vim](https://github.com/skywind3000/asyncrun.vim) Run Async Shell Commands in Vim 8.0 and Output to Quickfix Window
  * [codi.vim](https://github.com/metakirby5/codi.vim) The interactive scratchpad for hackers
  * [validator.vim](https://github.com/maralla/validator.vim) Check syntax on the fly asynchronously
  * [vim-grepper](https://github.com/mhinz/vim-grepper) Helps you win at grep.

# Vimscript
* [Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/)

  ```
  git clone https://github.com/JetBrains/ideavim.git
  ./gradlew buildPlugin
  - Install plugin from disk
  set surround, ys, cs, ds, 비쥬얼 모드에서의 S 모두 동작
  ```
