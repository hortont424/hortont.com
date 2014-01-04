import os

page_size = 10

www_prefix = "http://www.hortont.com/"
static_prefix = "http://files.hortont.com/www/"

if os.getcwd() == "/Users/hortont/src/hortont.com":
    www_prefix = "http://localhost:12345/"
    static_prefix = "http://localhost:12345/"

if os.environ["NOPREFIX"]:
    www_prefix = "/"
    static_prefix = "/"

blog_dir = "blog/"

blog_prefix = www_prefix + blog_dir

def w(u):
    return www_prefix + u

def categoryURLFromName(n):
    if n == "gnome":
        return "code/gnome"
    if n == "fooding":
        return "personal/fooding"
    if n == "video":
        return "school/video"
    return n

def categoryDisplayName(n):
    return n.replace("-"," ")