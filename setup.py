#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SetupTools : packaging du programme"""

try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
    except ImportError:
        from distutils.core import setup, find_packages

import pymaildev
import codecs
from setup_extends import *

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))


# expects an installed pypandoc: pip install pypandoc
# or/and sudo apt-get install pandoc
# from pypandoc.pandoc_download import download_pandoc
# download_pandoc()
def get_long_description():
    """..."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except (IOError, ImportError):
        import os
        return open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()


def my_version():
    """..."""
    from setuptools_scm.version import dirty_tag

    def clean_scheme(version):
        return dirty_tag(version) if version.dirty else '+clean'
    return {'local_scheme': clean_scheme}


setup(name=pymaildev.__fullname__,
      version=pymaildev.__version__,
      packages=find_packages(exclude=('pymaildev_tests')),  # ['pymaildev']
      long_description=get_long_description(),
      url='https://github.com/TristanEduProjet/PyMailDev',
      download_url='https://github.com/TristanEduProjet/PyMailDev/releases',
      author='Tristan, Olivier, Nicolas',
      author_email='...',
      # dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
      setup_requires=['wheel',
                      'setuptools_scm',
                      'pypandoc'],  # setuptools_scm_git_archive pytest-runner
      # use_scm_version=True, bug avec bdist_msi
      install_requires=['pyyaml>=3.10'],  # lib>=1.0.0 lib>=1.2.0,<=1.4.3x
      tests_require=['unittest-xml-reporting'],  # pytest pytest-cov pytest-xdist tox nose
      test_suite='pymaildev_tests',  # pymail_tests._MainTest.test_all
      cmdclass={'lint': LintCommand,
                'pylint': PylintCommand,
                'test_xml': TestXmlCommand},
      extras_require={
          'lint': ['pylint',
                   'pep8', 'pep257', 'pyflakes', 'pycodestyle', 'pydocstyle',
                   'flake8',
                   'pep8-naming',
                   'flake8_docstrings', 'flake8-todo', 'flake8-pytest',
                   'flake8-commas', 'flake8-author', 'flake8-debugger',
                   'flake8-module-imports', 'flake8-print', 'flake8-coding',
                   'flake8-deprecated', 'flake8-string-format', 'flake8-blind-except',
                   # hacking -> erreur version depends egg
                   # flake8-future
                   ],
          'debug': ['pdb', 'ipdb'],
      },
      entry_points={'console_scripts': [],  # 'pymail = pymaildev.__main__:main'
                    'gui_scripts': ['pymail = pymaildev.__main__:main']},
      platforms=['ALL', 'any'],
      # setup_requires = ['setup.cfg'],
      setup_cfg=True,
      )
