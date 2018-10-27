#-*- coding: utf-8 -*-
# Creation Date : 2018-10-27
# Created by : Antoine LeBel
from logs import log

import unittest

class TestLog(unittest.TestCase):
    def test_Log_ActionTest_Result(self):
        exp = "hello"
        result = self.log.say_hello()
        self.assertEqual(exp, result)

    def setUp(self):
        self.log = log.Log()
