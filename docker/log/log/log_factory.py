#-*- coding: utf-8 -*-
# Creation Date : 2018-11-03
# Created by : Antoine LeBel
import importlib
import sys

class LogFactory():
    PACKAGE = "log"
    def __init__(self):
        pass

    def create_log(self, log_name):
        try:
            module = importlib.import_module(self.PACKAGE + "." + log_name)
            class_name = self._parse_class_name(log_name)
            class_ = getattr(module, class_name)
            log_class = class_()
            return log_class
        except ImportError as e:
            print("Had import error with : %s".format(log_name) )
            sys.exit(1)

    def _parse_class_name(self, name):
        return name.title()
