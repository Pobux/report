#-*- coding: utf-8 -*-
# Creation Date : 2018-11-03
# Created by : Antoine LeBel
import unittest
from log import log_factory

class TestLog(unittest.TestCase):

    def test_log_Factory_createLog(self):
        lf = log_factory.LogFactory()

        exp = "Log!"
        result = lf.create_log("log").name
        self.assertEquals(exp, result)

    def test_log_Factory_Raise(self):
        lf = log_factory.LogFactory()
        self.assertRaises(SystemExit, lf.create_log, "nolog")
