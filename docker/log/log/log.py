# -*- coding: utf-8 -*-
# Creation Date : 2018-10-29
# Created by : Antoine LeBel

from log import root_dir
import json
import re
import os


class Log():
    def __init__(self, date="", heure="", host="", type="", logs=""):
        self.date = date
        self.heure = heure
        self.host = host
        self.type = type
        self.logs = logs

    def create_log(self):
        pass

    def fetch_log(self):
        pass


class Syslog(Log):
    def create_log(self):
        return "hello sys_log"

    def fetch_log(self):
        # soit on ouvre le fichier JSON existant, soit on charge le log avec read_syslog_to_json (à venir)
        with open("{}/database/syslogtext.json".format(root_dir()), "r") as f:
            db = json.load(f)
        return db

    def read_syslog_to_json(self):

        log_list = []
        os.system("cat /var/log/system.log > file.txt")
        entree = open("file.txt", "r")
        lign = entree.readline().strip()
        while lign != "":
            pattern = r'[a-zA-Z]+.[0-9]{2}.[0-9]{2}:[0-9]{2}:[0-9]{2}.+'
            line = entree.readline().strip()
            while not re.search(pattern, line):
                lign += line
                line = entree.readline().strip()
            log_list.append(self.build_log(lign))
            lign = line
        return log_list

    def build_log(self, lign):
        val = lign.split()
        date = val[0] + " " + val[1]
        time = val[2]
        user = val[3]
        le_type = val[4]
        log = lign
        return Log(date, user, time, le_type, log)


class Statlog(Log):
    def create_log(self):
        return "hello stat_log"

    def fetch_log(self):
        return "hello sys_log"
