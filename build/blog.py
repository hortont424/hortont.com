#!/usr/bin/env python3.2

import os
import fnmatch

import page
import util

def gen_control_files(dir):
    for root, dirs, files in os.walk(dir):
        for file in fnmatch.filter(files, "*.control"):
            yield os.path.join(root, file)

def gen_pages(files):
    for file in files:
        yield page.Page(file)

for p in gen_pages(gen_control_files("posts")):
    #output_file = open(os.path.join("output/blog/", p.filePath) + ".html", encoding="utf-8")
    #output_file.write(p.render("post"))

    print(p.render("post"))
