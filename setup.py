#!/usr/bin/env python

from distutils.core import setup

setup(name='sigmund-remote-logger',
      version='0.9.3',
      description='Sigmund is a remote logging service for Django.',
      author='Matt Caldwell',
      author_email='matt.caldwell@gmail.com',
      url='https://github.com/mattcaldwell/sigmund-remote-logger',
      packages=['sigmund', 'sigmund.logging',]
)
