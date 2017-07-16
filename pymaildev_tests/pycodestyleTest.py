#!python

import unittest
import pycodestyle

class CodeStyleTest(unittest.TestCase):
    def getStyle(self):
        return pycodestyle.StyleGuide(parse_argv=True, config_file='./../setup.cfg')
        #, quiet=True, config_file='/path/to/tox.ini', ignore=['E501']

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = self.getStyle()
        result = style.check_files("""['file1.py', 'file2.py']""")
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

#file_errors = pycodestyle.Checker(show_source=True).check_all()
#print("Found %s errors (and warnings)" % file_errors)

if __name__ == '__main__':
    style = CodeStyleTest().getStyle()
    report = style.check_files()
    if report.total_errors:
        raise SystemExit(1)
