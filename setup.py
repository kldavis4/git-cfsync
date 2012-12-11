#!/usr/bin/env python3

from distutils.core import setup

VERSION = '0.1'

setup(name='git-cfsync',
      author='Lee Verberne',
      author_email='lee@blarg.org',
      description='Keep configuration directories in sync using git',
      scripts=['git-cfsync'],
      version=VERSION
     )
