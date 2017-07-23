#!python
# -*- coding: utf-8 -*-

"""Compliance test (PEP8) of the package's code"""

import unittest
import pycodestyle


class CodeStyleTest(unittest.TestCase):
    """..."""

    @staticmethod
    def get_style():
        """..."""
        return pycodestyle.StyleGuide(quiet=True, parse_argv=True, config_file='./../setup.cfg')
        # , config_file='/path/to/tox.ini', ignore=['E501']

    def test_conformance(self):
        """Compliance test to PEP-8 (pyCodeStyle)."""
        style = self.get_style()
        result = style.check_files(['setup.py', 'setup_extends.py', 'pymaildev', 'pymaildev_tests'])  # ['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

# file_errors = pycodestyle.Checker(show_source=True).check_all()
# print("Found %s errors (and warnings)" % file_errors)


if __name__ == '__main__':
    style = CodeStyleTest().get_style()
    report = style.check_files()
    if report.total_errors:
        raise SystemExit(1)
