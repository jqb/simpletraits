# -*- coding: utf-8 -*-
import sys
import unittest

from simpletraits import baseclass, kwa, NIL


class User(baseclass):
    _arg = 'name', 'last_name'
    _kwa = 'passwd', kwa('default_passwd', default='admin')


class BaseClassTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Kuba", "Janoszek")

    def test_it_should_raise_AssertionError_if_theres_not_enough_args(self):
        self.assertRaises(AssertionError, User)
        self.assertRaises(AssertionError, User, "Kuba")  # there's no second argument

    def test_all_variables_listed_in_ARG_class_var_should_be_setup_on_instance(self):
        self.assertEqual(self.user.name, "Kuba")
        self.assertEqual(self.user.last_name, "Janoszek")

    def test_uninitialized_kwargs_should_be_setup_to_NIL(self):
        self.assertEqual(self.user.passwd, NIL)

    def test_ARG_and_KWA_class_variables_need_to_be_a_tuples(self):
        try:
            class Wrong_ARG_type(baseclass):
                _arg = "Wrong"
        except TypeError as e:
            pass  # this is expected
        else:
            self.fail('"_arg" has wrong type - exception should be raised')

        try:
            class Wrong_KWA_type(baseclass):
                _kwa = "Wrong"
        except TypeError as e:
            pass  # this is expected
        else:
            self.fail('"_kwa" has wrong type - exception should be raised')

    def test_default_keyword_arguments_should_be_used_if_not_provided(self):
        self.assertEqual(self.user.default_passwd, 'admin')

    def test_KWA_class_variable_can_be_a_dict(self):
        class KWATest(baseclass):
            _kwa = dict(
                counter = 0,
                name = "Kuba",
                last_name = "Janoszek",
            )
        test = KWATest()
        self.assertEqual(test.counter, 0)
        self.assertEqual(test.name, "Kuba")
        self.assertEqual(test.last_name, "Janoszek")


if __name__ == '__main__':
    unittest.main()
