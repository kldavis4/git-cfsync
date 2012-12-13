#!/usr/bin/env python3
#
# Copyright 2012 Lee Verberne <lee@blarg.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup

VERSION = '0.2'

setup(name='git-cfsync',
      author='Lee Verberne',
      author_email='lee@blarg.org',
      description='Keep configuration directories in sync using git',
      license='GPLv3',
      scripts=['git-cfsync'],
      version=VERSION
     )
