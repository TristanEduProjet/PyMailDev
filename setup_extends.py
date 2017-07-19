#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Part of setup.py"""

import distutils.log as log
import setuptools
import subprocess
import os
try:
    from setuptools import Command
    from setuptools.command.test import test
except ImportError:
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import Command
        from setuptools.command.test import test
    except ImportError:
        from distutils.cmd import Command
        from distutils.command.test import test


class PylintCommand(Command):
    """A custom command to run Pylint on all Python source files."""

    description = 'run Pylint on Python source files'
    user_options = [
        # The format is (long option, short option, description).
        ('pylint-rcfile=', None, 'path to Pylint config file'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.pylint_rcfile = ''

    def finalize_options(self):
        """Post-process options."""
        if self.pylint_rcfile:
            assert os.path.exists(self.pylint_rcfile), ('Pylint config file {0} does not exist.'.format(self.pylint_rcfile))
        else:
            if os.path.exists('pylintrc'):
                self.pylint_rcfile = 'pylintrc'
                print('Pylint default config file {0} found.'.format(self.pylint_rcfile))

    def run(self):
        """Run command."""
        command = ['pylint']  # /usr/bin/pylint
        if self.pylint_rcfile:
            command.append('--rcfile={0}'.format(self.pylint_rcfile))
        # command.append(os.getcwd())
        command.append("pymaildev")
        self.announce('Running command: {0}'.format(str(command), level=log.INFO))
        # subprocess.check_call(command)
        subprocess.call(command)


class TestXmlCommand(test):
    """A custom command to run Pylint on all Python source files."""

    description = 'run unit tests with xml runner after in-place build'
    # user_options = []

    def run_tests(self):
        """..."""
        from pymaildev_tests._MainTest import testall_xml
        testall_xml()

    def run(self):
        """..."""
        # import sys, subprocess
        # raise SystemExit(subprocess.call([sys.executable, '-m', 'xmlrunner', 'discover']))
        # self.run_command('pylint')
        test.run(self)


class LintCommand(Command):
    """Custom build command."""

    description = 'shortcut running pylint and flake8'
    user_options = []

    def initialize_options(self):
        """..."""
        pass

    def finalize_options(self):
        """..."""
        pass

    def run(self):
        """..."""
        self.run_command('pylint')
        self.run_command('flake8')
