## Markdown Latex Template QuickNote

Original Project Site: https://github.com/Wandmalfarbe/pandoc-latex-template

Usage
```shell
pandoc example.md -o example.pdf --from markdown --template eisvogel --listings
```

On top of document write
```md
---
title: "The Document Title"
author: [Example Author, Another Author]
date: "2017-02-20"
keywords: [Markdown, Example]
...

Here is the actual document text...
```