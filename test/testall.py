__author__ = 'bluzky'
import unittest

if __name__ == '__main__':
    all_test = unittest.defaultTestLoader.discover("./", "test_*.py")
    unittest.TextTestRunner().run(all_test)
    #all_test.run()