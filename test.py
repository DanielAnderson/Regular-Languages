import unittest
from project.testing import testNFA
from project.testing import testNFAVerifier
from project.testing import testDFAConversion

# To add test classes, add to this list
test_classes = [testNFA.TestNFA, testNFAVerifier.TestNFAVerifier, testDFAConversion.TestDFAConversion]

suites = []
for test_class in test_classes:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
    suites.append(suite)

suite = unittest.TestSuite(suites)
unittest.TextTestRunner(verbosity=2).run(suite)howdy partner
