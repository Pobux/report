
import importlib
import sys


class LogFactory():
    PACKAGE = "log.log"

    def __init__(self):
        pass

    def create_log(self, log_name, behavior):
        try:
            log = self.instantiate_class(log_name)
            log.setBehavior(behavior)
            return log
        except ImportError as e:
            print("Had import error with : %s".format(log_name))
            sys.exit(1)

    def _parse_class_name(self, name):
        return name.title()

    def create_behavior(self, behavior):
        return self.instantiate_class(behavior)

    def instantiate_class(self, log_name):
        module = importlib.import_module(self.PACKAGE)
        class_name = self._parse_class_name(log_name)
        class_ = getattr(module, class_name)
        return class_()
