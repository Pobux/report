#-*- coding: utf-8 -*-
# Creation Date : 2018-10-29
# Created by : Antoine LeBel
class Log():
    def __init__(self):
        self.name = "Log!"

    def create_log(self):
        pass


class SysLog(Log):
    def create_log(self):
        return "hello sys_log"


class StatLog(Log):
    def create_log(self):
        return "hello stat_log"