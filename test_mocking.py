from unittest import TestCase
from unittest.mock import patch
from datetime import datetime
from import_function import print_now
from import_module import print_timezone_now


class ImportMockTestCase(TestCase):
    # test import_function without mocking
    # test import_function mocking datetime.now
    # test import_function mocking import_function.now

    # test import_module without mocking
    # test import_module mocking datetime.now
    pass
