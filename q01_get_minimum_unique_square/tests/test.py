import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getfullargspec
from unittest import TestCase
from ..build import q01_get_minimum_unique_square


class TestRead_textfile(TestCase):

    def test_args(self):
        arg = getfullargspec(q01_get_minimum_unique_square).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (2, len(arg)))

    def test_number_1(self):
        self.assertEqual(q01_get_minimum_unique_square(4,16),3,"The Expected return Output does not match with the return Output")

    def test_number_2(self):
        self.assertEqual(q01_get_minimum_unique_square(24,27),1,"The Expected return Output does not match with the return Output")

    def test_number_3(self):
        self.assertEqual(q01_get_minimum_unique_square(81,100),2,"The Expected return Output does not match with the return Output")