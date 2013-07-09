from django.utils import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains # could be useful for future tests

from portal.testing.testcases import MobifyTestCase

class SeleniumTest(MobifyTestCase):
    templates = [
    ]

    def test(self):
        pass

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    main()
