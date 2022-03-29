import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AdShopCartPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_AdShopCart():  # test_ in the name is mandatory
        methods.setUp()
        methods.check_homepage()
        methods.sign_up()
        methods.check_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.delete_test_account()
        methods.log_in(locators.new_username, locators.new_password)
        methods.tearDown()