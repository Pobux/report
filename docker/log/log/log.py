#-*- coding: utf-8 -*-
# Creation Date : 2018-10-29
# Created by : Antoine LeBel

from log import root_dir
import json


class Log():
    def __init__(self):
        self.name = "Log!"

    def create_log(self):
        pass

    def fetch_log(self):
        pass


class Syslog(Log):
    def create_log(self):
        return "hello sys_log"

    def fetch_log(self):
        with open("{}/database/syslogtext.json".format(root_dir()), "r") as f:
            db = json.load(f)
        return db


class Statlog(Log):
    def create_log(self):
        return "hello stat_log"

    def fetch_log(self):
        return "hello sys_log"