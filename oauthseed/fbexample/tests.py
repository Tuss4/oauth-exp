from unittest import TestCase
from .utils import get_scope_params, get_fields_params


class UtilsTest(TestCase):

    def test_param_methods(self):
        self.assertEqual(get_scope_params(), 'email')
        self.assertEqual(get_fields_params(), 'email,first_name,last_name')
