#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import markdown
# from mdx_math import MathExtension

html_head_file = open("html_head.txt","r",encoding='utf-8')
html_head = html_head_file.read()
html_head_file.close()

html_tail_file = open("html_tail.txt","r",encoding='utf-8')
html_tail = html_tail_file.read()
html_tail_file.close()

# html_tail = "\n</body>\n</html>"
html_body = ""

# 所支持的复杂元素
exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
# exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc',MathExtension(enable_dollar_delimiter=True)]

file_dir = input("Enter the Mirror » ")

# os.chdir(file_dir)
# print(os.path.abspath(os.curdir))
# all_file = os.listdir()
# files = []

for filename in os.listdir(file_dir):
    if filename[-3:] == '.md':
        html_body_file = open(file_dir+filename,"r",encoding='utf-8')
        html_body_txt = html_body_file.read()
        html_body_file.close()

        md = markdown.Markdown(extensions = exts)
        html_body = md.convert(html_body_txt)

        html = html_head + html_body + html_tail
        # html_file = open(file_dir+filename[:-3]+".html","w",encoding='utf-8')
        html_file = open(file_dir+filename[:-3]+"","w",encoding='utf-8')
        html_file.write(html)
        html_file.close()
        print("{}☑️".format(filename[:-3]))
print("///// HTML fire Generated 🚀!!! /////")
