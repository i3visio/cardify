# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#   Cardify is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))

# Importing the local scrips for the setup and taking the new version number
import cardify
NEW_VERSION = cardify.__version__

# Depending on the place in which the project is going to be upgraded
from setuptools import setup
try:
    raise Exception('Trying to load the markdown manually!')    
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
except Exception:
    read_md = lambda f: open(f, 'r').read()

# Reading the .md file    
try:
    long_description = read_md(os.path.join(HERE,"README.md"))
except:
    long_description = ""
    
# Launching the setup
setup(    
    name="cardify",
    version=NEW_VERSION,
    description="Cardify - A set of GPLv3+ libraries to deal with carding information.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/cardify",
    license="COPYING",
    keywords = "python osint carding",
    scripts= [
        "scripts/cardify_launcher.py",            
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',   
        'Intended Audience :: Information Technology',      
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'Topic :: Communications',   
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',  
        'Topic :: Text Processing :: Markup :: HTML'                                 
    ],    
    packages=[
        "cardify", 
    ],
    long_description=long_description,
    install_requires=[
        "argparse",
    ],    
)
