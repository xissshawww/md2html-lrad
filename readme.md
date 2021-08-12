# Markdown to HTML for LRDA

```
.
├── html_head.txt
├── html_tail.txt
├── md2html-pandoc.sh
├── md2html.py
└── readme.md
```

## md2html.py

before using this, you should run:

```bash
pip install markdown
```

Change line35 by adding `.html` inside `""`before using.

Change `html_head.txt` and `html_tail.txt` for your needs.

## md2html-pandoc.sh

This bash file is using [pandoc](https://pandoc.org/) as a useful convert tool. So at first you should [install pandoc](https://pandoc.org/installing.html) for further use.

The standard .md file of pandoc require a nonempty `<title>` element. To specify a title, use 'title' in metadata or --metadata title="...".

Create or use a css file for your needs. I recommend [typora themes](https://theme.typora.io/) for daily use. 

In there i'm using lrda.css for [LRDA](https://deversnude.xyz/kaos/indoom.html) website.

x
