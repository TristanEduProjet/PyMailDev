import unittest
import doctest
import xmlrunner

#def additional_tests():
    #from . import *
    #suite = unittest.TestSuite()
    #suite.addTest (ArithTest())
    #suite.addTest (ArithTestFail())
    #return suite

#def suite():
    #return additional_tests()

if __name__ == "__main__":
    #with open('/path/to/results.xml', 'wb') as output: ...(output=output)
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
                  failfast=False, buffer=False, catchbreak=False)
    #unittest.TextTestRunner("""verbosity=2""").run(suite())
    #xmlrunner.XMLTestRunner().run(doctest.DocTestSuite())
