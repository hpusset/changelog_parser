#!/usr/bin/env python
# coding: utf8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An small CHANGELOG parser',
    'author': 'hpusset',
    'author_email': 'hpusset@gmail.com',
    'version': '0.1',
    'url': 'https://github.com/hpusset/changelog_parser',
    'install_requires': ['tox', 'pytest'],
    'packages': ['src/changelog_parser'],
    'scripts': [],
    'name': 'changelog_parser'
}

setup(**config)
