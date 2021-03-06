#!/usr/bin/env python3

from io import StringIO
from markdown import Markdown
import config
import os
import sys
import glob
from typing import List
from datetime import datetime

def get_article(root='content') -> List[str]:
    return glob.glob(root + '/**/*.md', recursive=True)


def parse_md(files: List[str]) -> str:
    s = ""
    s += config.TITLE + "\n"
    if config.UNDER_TITLE_TEXT:
        s += config.UNDER_TITLE_TEXT
        s += "\n"

    for file in files:
        s += '### [' + file.split('/')[-1] + f']({file}) \n'
        s += f'Last Modified: {datetime.fromtimestamp(os.path.getmtime(file)).strftime("%m-%d-%y")}' + '<br>'
        s += f'[Read on Github]({config.ORIGIN + "/blob/main/" + file}) for better experience if this document contains [Latex](https://en.wikibooks.org/wiki/LaTeX/Mathematics) Expressions\n'
        s += '#### Preview: '+'\n\n'
        # with open(file, mode='r') as f:
        #     s += unmark(f.read()[:config.DESC_LENGTH]).replace('\n', '<br>\n') + '...\n'

        s += "```\n"

        with open(file, mode='r') as f:
            s += unmark(f.read()[:config.DESC_LENGTH]) + '...\n'        
        
        s += "```\n"        
        
    s += "\n"
    s += config.FOOTER + "\n"
    s += "\n"
    return s


def write_index(s: str) -> None:
    with open('index.md', mode='w') as f:
        f.write(s)


def push():
    articles = get_article()
    articles = sorted(
        articles, key=lambda x: os.path.getmtime(x), reverse=True)
    parsed = parse_md(articles)
    write_index(parsed)
    os.system('git add .')
    os.system('git commit -a -m "Updated Blog"')
    os.system('git push')


def main(arg: List[str]) -> int:

    if len(arg) == 0:
        print("No option is given, quitting.\nHint: Use `./x.py push`.")
        exit(1)
    
    if arg[0] == 'push':
        push()
        exit(0)

    
    print("Invalid option")
    exit(1)


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)


if __name__ == '__main__':
    arg = sys.argv[1:]
    main(arg)
