# -*- coding: utf-8 -*-

# Copyright (C) 2008 Chris Dekter

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from distutils.core import setup

setup(
      name="autokey",
      version="0.54.5", 
      author="Chris Dekter",
      author_email="cdekter@gmail.com",
      url="http://autokey.sourceforge.net/",
      license="GPL v3",
      description="Text expansion and hotkey utility",
      long_description="""AutoKey is a text expansion/replacement and hotkey utility for Linux and X11.
It can receive keyboard events via several methods and uses X events to drive the expansions. 
It is designed to save time by automating repetitive typing tasks, among other things.""",
      #py_modules=["autokey", "configurationmanager", "expansionservice", "interface",
      #            "iomediator", "phrase", "phrasemenu", "ui"],
      package_dir={"autokey": "src/lib"},
      packages=["autokey", "autokey.plugin"],
      package_data={"autokey" : ["data/menus.xml"]},
      data_files=[("/usr/share/pixmaps", ["config/autokeyicon.svg"]),
                  ("/usr/share/applications", ["config/autokey.desktop"])],
      scripts=['autokey']
      #packages=["plugin"]
      )