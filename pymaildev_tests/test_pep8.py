#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pep8

class PEP8Test(unittest.TestCase):
    def getStyle(self):
        return pep8.StyleGuide(quiet=True, parse_argv=True, config_file='./../setup.cfg')
        #config_file=True

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = self.getStyle()
        result = pep8style.check_files("""['file1.py', 'file2.py']""")
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

#file_errors = pep8.Checker('testsuite/E27.py', show_source=True).check_all()
#print("Found %s errors (and warnings)" % file_errors)

if __name__ == '__main__':
    pep8style = PEP8Test().getStyle()
    report = pep8style.check_files()
    if report.total_errors:
        raise SystemExit(1)
