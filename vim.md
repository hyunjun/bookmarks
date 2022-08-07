Vim
===
* [Vim Koans](https://sanctum.geek.nz/arabesque/vim-koans/)
* [A vim Tutorial and Primer](https://danielmiessler.com/study/vim/)
* [openvim.com](http://www.openvim.com/)
* [hea-www.harvard.edu/~fine/Tech/vi.html](http://hea-www.harvard.edu/~fine/Tech/vi.html)
* [Vim Is The Perfect IDE](https://dev.to/allanmacgregor/vim-is-the-perfect-ide-e80)
* [vim 초 간단 매뉴얼](http://happyoutlet.tistory.com/11)
* [simple_vim_guide](https://github.com/johngrib/simple_vim_guide)
* [Let’s learn Vim! Part 1](https://hackernoon.com/lets-learn-vim-part-1-4752116637b4)
* [Let’s learn Vim! Part 2](https://hackernoon.com/lets-learn-vim-part-2-66b968f1551f)
* [Learn-Vim: A book for learning the Vim editor the smart way](https://github.com/iggredible/Learn-Vim)
* [How not to be afraid of Vim anymore - A curation of the most popular commands and how to use them](https://medium.freecodecamp.org/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae)
* [Basic Vim Commands Every Linux User Must Know](https://linuxhandbook.com/basic-vim-commands)
* [Vim 도대체 왜 쓰는가](https://bengi.kr/1349)
* [vim 입문자 핵심 단축키 공략](https://jybaek.tistory.com/928)
* [(05/30) "Vim 도대체 왜 쓰는가" 외 재미있는 개발 이야기](https://www.youtube.com/watch?v=LckoVnyWkX0)
* [8 Vim Tricks That Will Take You From Beginner to Expert | by Tyler Lum | The Startup | Medium](https://medium.com/swlh/8-vim-tricks-that-will-take-you-from-beginner-to-expert-817ff4870245)
* [7 Surprising Vim Tricks That Will Save You Hours | by Tyler Lum | Sep, 2020 | Level Up Coding](https://levelup.gitconnected.com/7-surprising-vim-tricks-that-will-save-you-hours-b158d23fe9b7)
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
* find
  * `:/<pattern>/` [substitute - Find and replace using regular expressions - Vi and Vim Stack Exchange](https://vi.stackexchange.com/questions/3115/find-and-replace-using-regular-expressions)
    * e.g. `:/micro[ ]\?frontend/` 'microfrontend' or 'micro frontend'
* help [vim help - 기계인간 John Grib](https://johngrib.github.io/wiki/vim/help/)
* join
  * [How to join lines without producing a space?](https://vi.stackexchange.com/questions/439/how-to-join-lines-without-producing-a-space)
* quickfix
  * [vim quickfix 기능 - 컴파일 에러 수정](http://sunyzero.tistory.com/223)
* pbcopy/pbpaste
  * `:a,b!pbcopy` copy line from a to b
  * [Mac OS X clipboard sharing](http://vim.wikia.com/wiki/Mac_OS_X_clipboard_sharing)
* replace
  * [Search_and_replace_in_multiple_buffers](http://vim.wikia.com/wiki/Search_and_replace_in_multiple_buffers)
  * example; remove all the spaces at the end of string

    ```
    :arg *.c
    :argadd *.h
    :argdo %s/[ ]\+$//ge | update
    ```
  * `ggVGu` change all the letters to lowercase [How to convert all text to lowercase in Vim](https://stackoverflow.com/questions/1102859/how-to-convert-all-text-to-lowercase-in-vim)
  * 개행 문자 입력 `^M (Ctrl+V, Ctrl+M)`
    * [Vim Vi 에서 ＾M 지우기, 행끝의 캐럿 M 기호 제거 방법](http://mwultong.blogspot.com/2007/08/vim-vi-m-m.html)
  * [lowercase <-> uppercase](http://www.linuxquestions.org/questions/linux-newbie-8/change-all-uppercase-to-lowercase-with-vi-633998/)

    ```
    :%s/.*/\L&/
    :%s/.*/\U&/
    ```
  * [VIM 치환 꼼수?](https://www.popit.kr/vim-%EC%B9%98%ED%99%98-%EA%BC%BC%EC%88%98/) 조건별 replace
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
  * [practice .vimrc example](https://gist.github.com/hyunjun/f4103247e247bc802b90#file-vimrc-example)
  * [practice vimrc](https://gist.github.com/hyunjun/f4103247e247bc802b90#file-vimrc-md)
  * [vimrc.io](http://vimrc.io/)
  * [Vim 사용자 정의 파일 타입 꾸미기](http://www.popit.kr/adding-custom-file-type-in-vim/) for syntax highlight
    * syntax highlighting이 되지 않는 경우
      * 보통 기본 vi나 vim-minimal만 설치된 경우 발생
      * vim-enhanced 설치
  * [vimrc-vundle-script](https://github.com/uyu423/vimrc-vundle-script/blob/master/README.md) 여러 리눅스 환경에서의 vimrc, vim plugin 파일 동기화를 위한 저장소
  * [Tweak Your Vim As A Powerful IDE. Vim is a joy to use, it is so well… | by Dery Rahman Ahaddienata | Level Up Coding](https://levelup.gitconnected.com/tweak-your-vim-as-a-powerful-ide-fcea5f7eff9c)
  * [set gvim font in .vimrc file](http://stackoverflow.com/questions/3316244/set-gvim-font-in-vimrc-file)
  * [5 lines I put in a blank .vimrc | Sword and Signals](https://swordandsignals.com/2020/12/13/5-lines-in-vimrc.html)
  * [vim 설정 파일을 주제별로 여러 파일로 분리하자 - 기계인간 John Grib](https://johngrib.github.io/wiki/vim/configure-split/)
  * gvim portable; `GVimPortable\App\DefaultData\settings\vimrc`
* window [Vim window - 기계인간 John Grib](https://johngrib.github.io/wiki/vim/window/)
* xmllint [Vim에서 XML 포맷팅하기](https://rein.kr/blog/archives/5551)
* [빔 편집기 한글화](http://vim-ko.github.io/)
* [Vim cheat sheet](http://csnipp.com/s/69/-Vim-Cheat-Sheet)
* [Vim Cheat Sheet](https://vim.rtorr.com/lang/ko)
* [100 Vim commands every programmer should know](http://www.catswhocode.com/blog/100-vim-commands-every-programmer-should-know)
* [Vim Genius](http://www.vimgenius.com/)
* [vimcasts.org](http://vimcasts.org/)
* [How to boost your Vim productivity](http://sheerun.net/2014/03/21/how-to-boost-your-vim-productivity/)
* [VIM: 8 Takeaways From One Year Of Typing](http://sankho.github.io/web_log/2015/08/02/vim-8-takeaways-from-one-year-of-typing.html)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Vim)
* [neovim](http://neovim.io/)
  * `~/.config/nvim/init.vim` [default location of configuration file](https://github.com/neovim/neovim/wiki/FAQ) just copy .vimrc as init.vim
  * [Oceanic Next theme for neovim](https://github.com/mhartington/oceanic-next)
  * [Vim-fork focused on extensibility and agility. Consider helping sustain Neovim development! https://salt.bountysource.com/teams/neovim](https://github.com/neovim/neovim)
  * [example of init.vim](https://gist.github.com/synasius/5cdc75c1c8171732c817)
  * [A guide to neovim](http://nerditya.com/code/guide-to-neovim/)
  * [A guide to modern Web Development with (Neo)vim](https://medium.freecodecamp.org/a-guide-to-modern-web-development-with-neo-vim-333f7efbf8e2)
  * [Setup Neovim like an IDE - YouTube](https://www.youtube.com/watch?v=65Wq4fjREUU)
  * [Step Up Your Game with Neovim. Why do I switch to VIM and use Neovim? | by Roderick Samuel Halim | Life At Moka | Medium](https://medium.com/life-at-moka/step-up-your-game-with-neovim-62ba814166d7)
  * [I switched from VSCode to Neovim - YouTube](https://www.youtube.com/watch?v=clFR9NfObvc)
  * [LunarVim - Installing Rolling Release, Walkthrough, Sample Configuration (IDE for Neovim) - YouTube](https://www.youtube.com/watch?v=NlRxRtGpHHk)
  * [navigator.lua: Navigate codes like a breeze. Exploring LSP and 🌲Treesitter symbols a piece of 🍰](https://github.com/ray-x/navigator.lua)
  * [neovim-dot-app - Mac OS X GUI for Neovim](https://github.com/rogual/neovim-dot-app)
  * [nvui: A modern frontend for Neovim](https://github.com/rohit-px2/nvui)
* [vim plugin to interact with tmux](https://github.com/benmills/vimux)
* [**What are the most amazing things that can be done with Vim?**](https://www.quora.com/What-are-the-most-amazing-things-that-can-be-done-with-Vim)
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
* [How do I edit current shell command in VI](http://apple.stackexchange.com/questions/88515/how-do-i-edit-current-shell-command-in-vi)
  * `set -o vi` - `esc` - `v`
  * `C-X C-E`
* [What's your best Vim related shell script?](https://www.reddit.com/r/vim/comments/3oo156/whats_your_best_vim_related_shell_script/)
* [Entering special characters](http://vim.wikia.com/wiki/Entering_special_characters)
* [regex - How to get Vim to highlight non-ascii characters?](https://stackoverflow.com/questions/16987362/how-to-get-vim-to-highlight-non-ascii-characters)
* [Highlight current line](http://vim.wikia.com/wiki/Highlight_current_line)
* [VIM adventures](http://vim-adventures.com/)
* [Vim에서 shell 사용하기](https://www.youtube.com/watch?v=_LJNar5tDfY)
* [<U+FEFF> character showing up in files. How to remove them?](http://stackoverflow.com/questions/7297888/ufeff-character-showing-up-in-files-how-to-remove-them) `:s/[\uFEFF]//g`
* [How to remove this symbol “^@” with vim?](http://superuser.com/questions/75130/how-to-remove-this-symbol-with-vim) `%s/<CTRL-2>//g` `%s/<CTRL-SHIFT-2>//g` (on Mac)
* [**vimgifs.com**](http://vimgifs.com)
* [Your problem with Vim is that you don't grok vi](http://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim/1220118#1220118)
* [Vim anti-patterns](https://sanctum.geek.nz/arabesque/vim-anti-patterns/)
* [exercise-2. vi를 효과적으로 연습하는 방법](https://www.youtube.com/watch?v=_dZk_jv5WlQ)
* [How to Do 90% of What Plugins Do (With Just Vim)](https://youtu.be/XA2WjJbmmoM)
  * ["Slides" and supplemental info from my August 3rd 2016 NYC Vim talk](https://github.com/mcantor/no_plugins)
  * [reddit/how_to_do_90_of_what_plugins_do_with_just_vim](https://www.reddit.com/r/vim/comments/5607lj/how_to_do_90_of_what_plugins_do_with_just_vim/)
* [cheatsheets/vimscript.html](http://ricostacruz.com/cheatsheets/vimscript.html)
* [Vim - Quick Reference Cheat Sheet](https://quickref.me/vim)
* [vim + tmux - OMG!Code](https://www.youtube.com/watch?v=5r6yzFEXajQ)
  * [Vim workshop](https://github.com/nicknisi/vim-workshop)
* [Vim with Windows | 한상곤 Sangkon Han | 2016.07](https://www.youtube.com/watch?v=pKrrw-mfzHg)
* [vi를 진정으로 이해해라](https://blog.weirdx.io/post/39518)
* [The Past and Future of Vim-go](https://speakerdeck.com/farslan/the-past-and-future-of-vim-go)
* [Creating Your Lovely Color Scheme](https://speakerdeck.com/cocopon/creating-your-lovely-color-scheme)
* [Vim, Me and Community](https://docs.google.com/presentation/d/14pViuMI_X_PiNwQD8nuGRG72GUqSeKDqoJqjAZWS39U/view#slide=id.p)
* [Why I love Vim: It’s the lesser-known features that make it so amazing](https://medium.freecodecamp.org/learn-linux-vim-basic-features-19134461ab85)
* [모든 앱에서 Vim을 사용하는 법 - QuickCursorKM과 vim-anywhere](https://nolboo.kim/blog/2018/02/17/vim-anywhere/)
* [Indenting Python with VIM](http://henry.precheur.org/vim/python.html)
* [You don’t need more than one cursor in vim](https://medium.com/@schtoeffel/you-don-t-need-more-than-one-cursor-in-vim-2c44117d51db)
* [**All I do is VIM VIM VIM**](http://engineering.pivotal.io/post/all-i-do-is-vim/)
* [Vim은 어디서 왔나](https://blog.koriel.kr/where-vim-came-from/)
* [VIM을 이용하여 각 줄의 마지막 공백(Whitespace) 제거하기](http://kkamagui.tistory.com/904)
* [Vim 공백 문자 조작 설정 - 기계인간 John Grib](https://johngrib.github.io/wiki/vim/set-empty-chars/)
* [Mastering the Vim Language](https://www.youtube.com/watch?v=wlR5gYd6um0)
* [mastering-vim-quickly](https://jovicailic.org/mastering-vim-quickly/)
* [Let Vim Do the Typing](https://www.youtube.com/watch?v=3TX3kV3TICU)
* [Vim을 IDE처럼 사용하기](http://blog.b1ue.sh/2016/10/09/vim-ide/)
* [How to Do 90% of What Plugins Do (With Just Vim)](https://www.youtube.com/watch?v=XA2WjJbmmoM)
* [**Talk on going mouseless with Vim, Tmux, and Hotkeys**](https://www.youtube.com/watch?v=E-ZbrtoSuzw)
* [Vim Makes Everything Better, Especially Your File Manager And Shell!](https://www.youtube.com/watch?v=a4scYdubKbo)
* [Openwest 2015 - Erik Falor - "From Vim Muggle to Wizard in 10 Easy Steps" (8)](https://www.youtube.com/watch?v=MquaityA1SM)
* [Vim 교정학원 후기](https://lqez.github.io/blog/vimrc-2019.html)
* [Vim 취약점 발견](https://jybaek.tistory.com/807)
* [History and effective use of Vim](https://begriffs.com/posts/2019-07-19-history-use-vim.html)
* [Vim + Python + Bash - The Perfect Trio for Productivty](https://www.youtube.com/watch?v=pIgej7rE70E)
* [vi 에디터 사용법 (vim editor)](https://blog.lael.be/post/7321)
* [Chase Your VIM Demons Away](https://medium.com/better-programming/chase-your-vim-demons-away-4405168effc8)
* [Editors (Vim)](https://missing.csail.mit.edu/2020/editors/)
* [Portable Shell and VIM Customization | by Jeremy Cheng | Jul, 2020 | Level Up Coding](https://levelup.gitconnected.com/portable-shell-and-vim-customization-9c054d80f5ca)
* [**(Linux) Vim 에디터 다양한 기능 설명 및 C++/Python 개발 환경설정 · Edward Im**](https://edward0im.github.io/technology/2020/09/17/vim/)
* [Vim for humans | Free price ebook](https://vimebook.com/en)
* [(리눅스 업스킬 도전 #6) vim 익숙해지기](https://jhrogue.blogspot.com/2020/09/6-vim.html)
* [Vim Isn’t That Scary. Here are 5 free resources you can use… | by Fatos Morina | Better Programming | Medium](https://medium.com/better-programming/vim-isnt-that-scary-here-are-5-free-resources-you-can-use-to-learn-it-5bba109a7422)
* [Switching from Visual Studio Code to Vim: the basics. | by Laura Davies | The Startup | Medium](https://medium.com/swlh/switching-from-visual-studio-code-to-vim-the-basics-f2bb40f5a8a3)
* [3½ Reasons Why You Should Be Using Vim | by Tate Galbraith | Better Programming | Medium](https://medium.com/better-programming/3%C2%BD-reasons-why-you-should-be-using-vim-8202360afa3)
* [Vim for Developers: Part 0 — Why Vim? | by David Ondrich | Level Up Coding](https://levelup.gitconnected.com/vim-for-developers-part-0-why-vim-95e68dc5d3a1)
* [Vim for Developers: Part 1 — The Basics | by David Ondrich | Analytics Vidhya | Medium](https://medium.com/analytics-vidhya/vim-for-developers-part-1-the-basics-663619ca122a)
* [Vim for Developers: Part 2 — Advanced Basics | by David Ondrich | The Startup | Medium](https://medium.com/swlh/vim-for-developers-part-2-advanced-basics-857c0dbda905)
* [Why (and How) I Use Vim. When I started programming I never… | by Mark Lavin | Level Up Coding](https://levelup.gitconnected.com/why-and-how-i-use-vim-da322260aa6c)
* [Vim 단축키 정리 :: Outsider's Dev Story](https://blog.outsider.ne.kr/540)
* [빔 교정학원 VIMRC 2022 - YouTube](https://www.youtube.com/watch?v=8wQ7c2Tbtkw)
* [Learn Vim the Simple Way](https://www.vimified.com/)
* [간단한 16진수 변환기를 만들고 vim에서 사용하기 - YouTube](https://www.youtube.com/watch?v=oa8lc6qOo5A)

# Book
* [Use Vim Like A Pro](https://leanpub.com/VimLikeAPro/read_full)

# Library
* [pyvim - An implementation of Vim in Python](https://github.com/jonathanslenders/pyvim)
* [quick.nvim: A very fast Lua based Neovim configuration that uses coc.nvim for intellisense](https://github.com/albingroen/quick.nvim)
  * [quick.nvim | A fast, modern and reliable Neovim configuration - YouTube](https://www.youtube.com/watch?v=OhbgZbORFd4)
* [vim-airline](https://github.com/vim-airline) lean & mean status/tabline for vim that's light as air
* [Vim Bootstrap - A generator which provides a simple method of generating a .vimrc configuration for vim](http://www.vim-bootstrap.com/)
* [vimflowy: An open source productivity tool drawing inspiration from workflowy and vim](https://github.com/WuTheFWasThat/vimflowy)
* [vim-galore - Everything you need to know about Vim](https://github.com/mhinz/vim-galore/)
* [vim-quickui - The missing UI extensions for Vim 8.2 (and NeoVim 0.4) !!](https://github.com/skywind3000/vim-quickui)
* [vim-rest-console: A REST console for Vim](https://github.com/diepm/vim-rest-console)
  * [vim-rest-console 사용법 - 기계인간 John Grib](https://johngrib.github.io/wiki/vim/rest-console/)
* [vim.so - Learn and Master Vim faster with interactive exercises](https://www.vim.so/)
  * [How I made $10k in one month from an online vim course](https://www.slip.so/blog/how-I-made-10k-teaching-vim)
* [vimwiki - A Personal Wiki For Vim](https://github.com/vimwiki/vimwiki)
  * [Vimwiki + Jekyll + Github.io로 나만의 위키를 만들자](https://johngrib.github.io/blog/2017/12/06/my-wiki/)

# Plugin
* [Vim Awesome](https://vimawesome.com/)
* [Python으로 vim plugin 만들기](http://www.slideshare.net/mysqlguru/python-vim-plugin)
* [레거시 코드를 파괴하는 Vim 벽돌 깨기](http://woowabros.github.io/tools/2017/07/06/vim-game-code-break.html)
* [IntelliJ 의 VIM 플러그인 마개조하기](http://woowabros.github.io/tools/2016/06/18/ideavim-customize-00.html)
* [Vi를 좋아하시는 분들을 위하여](http://greatkim91.tistory.com/m/196)
* [How to Configure Vim like VSCode - YouTube](https://www.youtube.com/watch?v=gnupOrSEikQ)
* [4 Vim Plugins to Boost Your Programming Efficiency | by Tate Galbraith | Better Programming | Medium](https://medium.com/better-programming/4-vim-plugins-to-boost-efficiency-6922add12e83)
* [Going through my Dev Setup - YouTube](https://www.youtube.com/watch?v=gMcGb55bsaE)
* [anderson.vim - Dark vim colorscheme based on colors from Wes Anderson films](https://github.com/gilgigilgil/anderson.vim)
* autosave
  * [Vim에서 저장하는 방법 - 자동 저장](https://nolboo.kim/blog/2017/09/14/vim-write-autosave/)
* [coc.nvim - 기계인간 John Grib](https://johngrib.github.io/wiki/vim/coc-nvim/)
* [context.vim: Vim plugin that shows the context of the currently visible buffer contents](https://github.com/wellle/context.vim)
* [diminactive.vim This is a plugin for Vim to dim inactive windows](https://github.com/blueyed/vim-diminactive)
* [EditorConfig plugin for Vim http://editorconfig.org](https://github.com/editorconfig/editorconfig-vim)
  * [EditorConfig](http://editorconfig.org/) 서로 다른 IDE에서 코딩 스타일을 통일
* [Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [Plugin completion using VimAwesome API](https://gist.github.com/junegunn/5dff641d68d20ba309ce)
* [Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile. https://powerline.readthedocs.org ](https://github.com/powerline/powerline)
* [Snake - Full Python Scripting in Vim](https://github.com/amoffat/snake)
* [vim-dadbod - Modern database interface for Vim](https://github.com/tpope/vim-dadbod)
* [vim-flake8](https://github.com/nvie/vim-flake8)
* [vim-f-hangul](https://johngrib.github.io/wiki/vim-f-hangul/)
* [vim-github-dashboard - 그래, 가끔 "Vim에서" GitHub을 보자!](http://tech.kakao.com/2016/03/03/vim-github-dashboard/)
* [vim-go - Go development plugin for Vim](https://github.com/fatih/vim-go)
  * [Go Development with Vim-go](https://www.youtube.com/watch?v=7BqJ8dzygtU)
* [vim-pathogen](https://github.com/tpope/vim-pathogen)
* [vim-plug - Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [vim-python-mode](https://github.com/klen/python-mode)
* [vim scripts](http://vim-scripts.org/vim/scripts.html)
* [Vimwiki 사용법](https://johngrib.github.io/wiki/vimwiki/)
* [Vundle](https://github.com/VundleVim/Vundle.vim)
  * [vim 사용자를 위한 플러그인 매니저 vundle 을 소개 합니다](https://kldp.org/node/125263?destination=node%2F125263)
  * [practice - vundle + vim-flake8 install example](https://gist.github.com/hyunjun/f4103247e247bc802b90)
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
* [Yode-Nvim - Focused Code Editing - YouTube](https://www.youtube.com/watch?v=4jXGKmBrD5g)
* [youcompleteme - A code-completion engine for Vim http://valloric.github.io/YouCompleteMe ](https://github.com/Valloric/YouCompleteMe)
  * [youcompleteme를 python3로 구동하기](https://johngrib.github.io/wiki/vim-ycm-python3/)

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
