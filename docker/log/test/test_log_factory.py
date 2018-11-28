#-*- coding: utf-8 -*-
# Creation Date : 2018-11-03
# Created by : Antoine LeBel
import unittest
from log import log_factory

class TestLogFactory(unittest.TestCase):

    def test_log_Factory_createLog(self):
        thrown = False
        try:
            lf = log_factory.LogFactory()
            lf.create_log("syslog", "text")
        except ImportError as e:
            thrown = True
        self.assertFalse(thrown)

    def test_log_Factory_parse_class_name(self):

        lf = log_factory.LogFactory()
        exp = "Syslog"
        result = lf._parse_class_name("syslog")
        self.assertEquals(exp, result)

    def test_log_factory_instantiate_class(self):
        lf = log_factory.LogFactory()
        _class = lf.instantiate_class("syslog")
        self.assertIsNotNone(_class)



    #def test_log_Factory_Raise(self):
        #lf = log_factory.LogFactory()
        #self.assertRaises(SystemExit, lf.create_log, "nolog")
