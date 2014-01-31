#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'steve@chigeek.com'
SITENAME = u'La DoSa Nostra'
SITEURL = ''

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
THEME = 'theme'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DIRECT_TEMPLATES = (
    'index', 
    'tags', 
    'categories', 
    'archives',
    'news',
)

PAGINATED_DIRECT_TEMPLATES = (
    'index',
    'news',
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enable code highlighting     
MD_EXTENSIONS = (['codehilite(css_class=codehilite)'])