#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SetupTools : packaging du programme
"""

from setuptools import setup, find_packages
import pymaildev

setup(name = pymaildev.__fullname__,
      version = pymaildev.__version__,
      author = "Tristan, Olivier, Nicolas",
      keywords = 'mail email dev devel developer',
      classifiers = ['Operating System :: OS Independent',
                     'Natural Language :: French',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Topic :: Communications :: Email',
                     'Topic :: Desktop Environment',
                     'License :: Other/Proprietary License',
                     'Development Status :: 1 - Planning'],
      packages = find_packages(), #['pymaildev']
      include_package_data = True,
      url = 'https://github.com/TristanEduProjet/PyMailDev',
      description = 'Python mail client by developpers',
      long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
      plateformes = 'ALL',
      #entry_points = {'console_scripts': ['pymail = pymaildev.py:func']},
      #install_requires = ['lib>=1.0.0', 'lib>=1.2.0,<=1.4.3']
      )
