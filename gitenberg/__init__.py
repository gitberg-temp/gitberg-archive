#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from .book import Book
from .clone import clone
from .config import ConfigFile
from .config import check_config
from .library import main as library
from .workflow import upload_all_books

__title__ = 'gitberg'
__appname__ = 'gitberg'
__version__ = '0.0.10'
__copyright__ = 'Copyright 2012-2015 Seth Woodworth'
