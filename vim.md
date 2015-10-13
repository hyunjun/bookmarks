Vim
===
* [A vim Tutorial and Primer](https://danielmiessler.com/study/vim/)
* buffers
  * [How do I close a single buffer (out of many) in Vim?](http://stackoverflow.com/questions/1269648/how-do-i-close-a-single-buffer-out-of-many-in-vim)
* ctags
  * .vimrc에 `set tags+=/path/to/tags`를 추가 or `:set tags+=path/to/tags`
* replace
  * [Search_and_replace_in_multiple_buffers](http://vim.wikia.com/wiki/Search_and_replace_in_multiple_buffers)
  * example; remove all the spaces at the end of string

    ```
    :arg *.c
    :argadd *.h
    :argdo %s/[ ]\+$//ge | update
    ```
* splits
  * horizontal splits `ctrl + w + J` <-> vertical splits `ctrl + w + H`
* :vimgrep
  * `:vimgrep [string to find] [target file]`
    * e.g. `:vimgrep /<emphasis>vim<\/emphasis>/ *.xml`
  * [jump command](http://stackoverflow.com/questions/7880372/how-to-jump-between-patterns-when-using-vimgrep-quickfix-list)
    * `:cn`, `:cp` jump to the next and previous entry
    * `:cnf`, `:cpf` jump to the next and previous file
    * `:cr`, `:cla` go to the beginning and end of the quickfix list
    * `:col`, `:cnew` iterate through historical quickfix lists
* [빔 편집기 한글화](http://vim-ko.github.io/)
* [Vim cheat sheet](http://csnipp.com/s/69/-Vim-Cheat-Sheet)
* [100 Vim commands every programmer should know](http://www.catswhocode.com/blog/100-vim-commands-every-programmer-should-know)
* [Vim Genius](http://www.vimgenius.com/)
* [vimcasts.org](http://vimcasts.org/)
* [How to boost your Vim productivity](http://sheerun.net/2014/03/21/how-to-boost-your-vim-productivity/)
* [VIM: 8 Takeaways From One Year Of Typing](http://sankho.github.io/web_log/2015/08/02/vim-8-takeaways-from-one-year-of-typing.html)
* [joinc](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/Vim)
* [neovim](http://neovim.org/)
  * [neovim-dot-app - Mac OS X GUI for Neovim](https://github.com/rogual/neovim-dot-app)
  * [Oceanic Next theme for neovim](https://github.com/mhartington/oceanic-next)
* [vim plugin to interact with tmux](https://github.com/benmills/vimux)
* **[What are the most amazing things that can be done with Vim?](https://www.quora.com/What-are-the-most-amazing-things-that-can-be-done-with-Vim)**
* [Use Vim everywhere you've always wanted to](https://github.com/cknadler/vim-anywhere)
* [History Is a Tree](http://ideasintosoftware.com/history-is-a-tree/)
* [You have decided to use vi as your main text editor. A few tricks that will help you improve your skills](https://david.padilla.cc/posts/12-you-have-decided-to-use-vi-as-your-main-text-editor-a-few-tricks-to-improve-your-skills)
* [Auto-Reload Your Vimrc](http://www.bestofvim.com/tip/auto-reload-your-vimrc/)
* [Vim Tips For Intermediate Users](http://ideasintosoftware.com/vim-productivity-tips/) relative line numbers, saving on focus lost, and vertical buffers
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

# Plugin
* [anderson.vim - Dark vim colorscheme based on colors from Wes Anderson films](https://github.com/gilgigilgil/anderson.vim)
* [Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)
* [Plugin completion using VimAwesome API](https://gist.github.com/junegunn/5dff641d68d20ba309ce)
* [Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile. https://powerline.readthedocs.org/en/latest/](https://github.com/powerline/powerline)
* [Snake - Full Python Scripting in Vim](https://github.com/amoffat/snake)
* [vim-go - Go development plugin for Vim](https://github.com/fatih/vim-go)
* [vim-plug - Minimalist Vim Plugin Manager](https://github.com/junegunn/vim-plug)

# Vimscript
* [Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/)
