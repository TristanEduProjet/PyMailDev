#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Point d'appel principal des tests."""

import unittest
# import doctest
import xmlrunner

from . import *

"""def additional_tests():
    #from . import *
    #suite = unittest.TestSuite()
    #suite.addTest (ArithTest())
    #suite.addTest (ArithTestFail())
    #return suite"""

"""def suite():
    #return additional_tests()"""


def testall():
    """..."""
    unittest.main(module=None, failfast=False, buffer=False, catchbreak=False)
    # unittest.TextTestRunner("""verbosity=2""").run(suite())


def testall_xml():
    """..."""
    # with open('/path/to/results.xml', 'wb') as output: ...(output=output)
    # unittest.main(module=None,
    #               testRunner=,
    #               failfast=False, buffer=False, catchbreak=False)
    # xmlrunner.XMLTestRunner().run(doctest.DocTestSuite())
    xmlrunner.XMLTestRunner(output='test-reports').run(unittest.TestLoader().discover('.'))


if __name__ == "__main__":
    testall_xml()
