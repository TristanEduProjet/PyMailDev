#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SetupTools : packaging du programme
"""

from setuptools import setup, find_packages
import os
import pymaildev
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

setup(name = pymaildev.__fullname__,
      version = pymaildev.__version__,
      author = "Tristan, Olivier, Nicolas",
      author_email = '...',
      keywords = 'mail email dev devel developer',
      classifiers = ['Operating System :: OS Independent',
                     'Natural Language :: French',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Intended Audience :: Developers',
                     'Topic :: Communications :: Email',
                     'Topic :: Desktop Environment',
                     'License :: Other/Proprietary License',
                     'Development Status :: 1 - Planning'],
      packages = find_packages(), #['pymaildev']
      include_package_data = True,
      url = 'https://github.com/TristanEduProjet/PyMailDev',
      download_url = 'https://github.com/TristanEduProjet/PyMailDev/releases',
      description = 'Python mail client by developpers',
      long_description = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read(),
      platforms = 'ALL'
      #entry_points = {'console_scripts': ['pymail = pymaildev.py:func']},
      #install_requires = ['lib>=1.0.0', 'lib>=1.2.0,<=1.4.3']
      )
