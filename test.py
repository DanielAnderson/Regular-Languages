import unittest
from project.testing import testNFA

suite = unittest.defaultTestLoader.loadTestsFromTestCase(testNFA.TestNFA)
unittest.TextTestRunner(verbosity=2).run(suite)
