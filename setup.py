#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SetupTools : packaging du programme
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
import pymaildev
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

# expects an installed pypandoc: pip install pypandoc
# or/and sudo apt-get install pandoc
#from pypandoc.pandoc_download import download_pandoc
#download_pandoc()
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    import os
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()

setup(name = pymaildev.__fullname__,
      version = pymaildev.__version__,
      author = "Tristan, Olivier, Nicolas",
      author_email = '...',
      keywords = 'mail email dev devel developer',
      classifiers = ['Operating System :: OS Independent',
                     'Operating System :: MacOS',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: Unix',
                     'Operating System :: POSIX :: Linux',
                     'Environment :: Win32 (MS Windows)',
                     'Environment :: MacOS X',
                     'Natural Language :: French',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.0',
                     'Programming Language :: Python :: 3.1',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Intended Audience :: Developers',
                     'Intended Audience :: End Users/Desktop',
                     'Topic :: Communications :: Email',
                     'Topic :: Desktop Environment',
                     'Framework :: Flake8',
                     'License :: Other/Proprietary License',
                     'License :: Free For Home Use',
                     'License :: Free for non-commercial use',
                     'Development Status :: 1 - Planning'],
      packages = find_packages(), #['pymaildev']
      include_package_data = True,
      #zip_safe=False,
      url = 'https://github.com/TristanEduProjet/PyMailDev',
      download_url = 'https://github.com/TristanEduProjet/PyMailDev/releases',
      description = 'Python mail client by developpers',
      long_description = long_description,
      platforms = 'ALL', #'any' #['any']
      entry_points = {
          #'console_scripts': ['pymail = pymaildev.__main__:main'],
          'gui_scripts': ['pymail = pymaildev.__main__:main']
      },
      #install_requires = ['lib>=1.0.0', 'lib>=1.2.0,<=1.4.3']
      #dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
      #extra_requires={'':['']}
      test_suite='pymaildev_tests', #pymail_tests._MainTest.test_all
      tests_require = ['unittest-xml-reporting',
                       #differents lint
                       'pylint',
                       'pep8', 'pep257'
                       'pyflakes', 'hacking'
                       'pycodestyle', 'pydocstyle',
                       #Flake8 & plugins
                       'flake8',
                       'pep8-naming',
                       'flake8_docstrings', 'flake8-future', 'flake8-todo',
                       'flake8-pytest', 'flake8-commas', 'flake8-author',
                       'flake8-debugger', 'flake8-module-imports', 'flake8-print',
                       'flake8-coding', 'flake8-deprecated', 'flake8-string-format',
                       'flake8-blind-except']
      )
