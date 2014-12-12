#!/usr/bin/python
# -*- coding: utf-8 -*-

from io import open
from os import path, listdir
from time import strftime, ctime, localtime
from sys import version

from bottle import route, error, abort, run, static_file, response, template, __version__
from markdown2 import markdown

CONTENT = './content'
STATIC = './static'

def get_title(filepath):
    try:
        with open(filepath) as f:
            title = f.readline()
            if not title:
                title = '[[ Untitled ]]'
    except IOError:
        return '[[ *** Error: FILE NOT FOUND ]]'
    else:
        return title

@error(404)
def error_404(error):
    return '404: FILE NOT FOUND!'

@error(500)
def error_500(error):
    return '500 - Something gone wrong... %s' % error

@route('/')
def index():
    ls = listdir(CONTENT)
    last_mod = lambda f: path.getmtime(path.abspath(path.join(CONTENT, f)))
    articles =\
        reversed(
        sorted(
        [(last_mod(f), f, get_title(path.join(CONTENT, f))) for f in ls]))
    articles = [(localtime(t), f, title) for (t, f, title) in articles]
    return template('index', content=articles, title=None)


@route('/static/<file:path>')
def static(file):
    return static_file(file, root=STATIC)

@route('/doc/<file:path>')
def doc(file):
    file_path = path.join(CONTENT, file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        mod_time = strftime('%Y-%m-%dT%H:%M',
                 localtime(path.getmtime(file_path)))
        mod_time_f = ctime(path.getmtime(file_path))
    except IOError:
        abort(404)
    except:
        abort(500)
    else:
        html = markdown(content)
        return template('doc', content=html, title=get_title(file_path),
                        mod_time=mod_time, mod_time_f=mod_time_f, file_name=file)

@route('/raw/<file:path>')
def raw(file):
    file_path = path.join(CONTENT, file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except IOError:
        abort(404)
    except:
        abort(500)
    else:
        response.content_type = 'text/plain; charset=utf8'
        return content

@route('/about')
def about():
    last_update = ctime(path.getmtime('run.py'))
    ls = listdir(CONTENT)
    ls.sort()
    return template('about', title='À propos', py_ver=version,
                     ls=ls, bottle_ver=__version__,
                     last_update=last_update)


if __name__ == '__main__':
    run(host='0.0.0.0', port=5000, debug=True)
