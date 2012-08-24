# -*- coding: utf-8 -*-

import sys

py = sys.version_info
py3k = py >= (3, 0, 0)

default_encoding = sys.getfilesystemencoding()
if default_encoding.lower() == 'ascii':
    default_encoding = 'utf-8'

from codecs import open

if py3k:
    is_bytes = lambda s: isinstance(s, bytes)
    is_unicode = lambda s: isinstance(s, str)
    is_str = lambda s: isinstance(s, (bytes, str))
    encode = lambda s, encoding: bytes(s, encoding)
    unistr = str
else:
    is_bytes = lambda s: isinstance(s, str)
    is_unicode = lambda s: isinstance(s, unicode)
    is_str = lambda s: isinstance(s, basestring)
    unistr = unicode
    encode = lambda s, encoding: s.encode(encoding)

to_bytes = lambda s, encoding=None: \
    encode(s, encoding or default_encoding) if is_unicode(s) else s
to_unicode = lambda s, encoding=None: \
    s if is_unicode(s) else s.decode(encoding or default_encoding)
B = to_bytes
U = lambda s: to_bytes(s).decode('raw_unicode_escape')


if py3k:
    raw_input = input
else:
    raw_input = raw_input


if py3k:
    from urllib.request import urlopen, Request, build_opener, HTTPCookieProcessor
    from urllib.parse import urlencode
    from http import cookiejar as cookielib
    from http.cookies import SimpleCookie
else:
    from urllib2 import urlopen, Request, build_opener, HTTPCookieProcessor
    from urllib import urlencode
    import cookielib
    from Cookie import SimpleCookie

if py3k:
    from io import BytesIO as StringIO
else:
    from cStringIO import StringIO

if py3k:
    _map = map
    _filter = filter
    _zip = zip
    map = lambda *x: list(_map(*x))
    filter = lambda *x: list(_filter(*x))
    zip = lambda *x: list(_zip(*x))
else:
    map = map
    filter = filter
    zip = zip
