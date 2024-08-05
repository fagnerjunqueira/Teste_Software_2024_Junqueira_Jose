import unittest
import all_tests as all
testSuite = all.create_test_suite()
text_runner = unittest.TextTestRunner().run(testSuite)