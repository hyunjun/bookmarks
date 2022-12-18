효율성이 배가되는 WSL2 가이드북
===============================
<img src="wsl2/2.jpg" alt="title" width="400"/>

* [Windows-Subsystem-for-Linux-2-WSL-2-Tips-Tricks-and-Techniques: Windows Subsystem for Linux 2 (WSL 2) Tips, Tricks, and Techniques, published by Packt](https://github.com/PacktPublishing/Windows-Subsystem-for-Linux-2-WSL-2-Tips-Tricks-and-Techniques)

<img src="wsl2/4.jpg" alt="title" width="400"/>

[bash-git-prompt: An informative and fancy bash prompt for Git users](https://github.com/magicmonty/bash-git-prompt)

<img src="wsl2/5.jpg" alt="title" width="400"/>

# jq 사용
<img src="wsl2/6.jpg" alt="title" width="400"/>

> `❯ echo '[1,2,"testing"]' | jq`

<img src="wsl2/7.jpg" alt="title" width="400"/>

> `❯ cat ./wsl-book.json | jq ".parts[].name"`

<img src="wsl2/8.jpg" alt="title" width="400"/>

```
❯ cat/wsl-book.json | jq ".title"

❯ BOOK_TITLE=$(cat /wsl-book.json | jq ".title" -r)

❯ cat ./wsl-book.json | jq ".parts"

❯ cat ./wsl-book.json | jq ".parts[0].name"
```

<img src="wsl2/9.jpg" alt="title" width="400"/>

```
❯ cat ./wsl-book.json | jq ".parts[].name"

❯ cat ./wsl-book.json | jq '.parts[] | {name}'
```

<img src="wsl2/10.jpg" alt="title" width="400"/>

```
❯ cat ./wsl-book.json | jq '.parts[] | {name: .name, chapter_count: .chapters | length}'

❯ cat ./wsl-book.json | jq '[.parts[] | {name: .name, chapters: [.chapters[] | .title]}]'
```

# 파워셸과 JSON을 엮어서 일하기
<img src="wsl2/11.jpg" alt="title" width="400"/>

> [Install PowerShell on Linux - PowerShell | Microsoft Learn](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux?view=powershell-7.3&viewFallbackFrom=powershell-7)