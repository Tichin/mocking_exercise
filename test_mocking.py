from unittest import TestCase
from unittest.mock import patch
from import_function import make_breakfast
from import_module import make_dessert


class ImportMockTestCase(TestCase):
    # test make_breakfast
    print("Calling make_donut() when imported as FUNCTION")
    print("We are not going to mock the return value")
    make_breakfast()

    # test make_breakfast mocking module
    def make_banana():
        print("Made a banana!")

    with patch('baking.make_donut', make_banana):
        print("")
        print("Calling make_donut() when imported as FUNCTION")
        print("We are mocking baking.make_donut to make a banana instead")
        print("NOTE: This should fail to make a banana and make a donut instead")
        make_breakfast()

    # test make_breakfast mocking function
    def make_banana():
        print("Made a banana!")

    with patch('import_function.make_donut', make_banana):
        print("")
        print("Calling make_donut() when imported as FUNCTION")
        print("We are mocking import_function.make_donut to make a banana instead")
        make_breakfast()

    # test make_dessert without mocking
    print("")
    print("Calling make_donut() when imported as MODULE")
    print("We are not going to mock the return value")
    make_dessert()

    # test make_dessert mocking module
    def make_banana():
        print("Made a banana!")

    with patch('baking.make_donut', make_banana):
        print("")
        print("Calling make_donut() when imported as MODULE")
        print("We are mocking baking.make_donut to make a banana instead")
        make_dessert()
