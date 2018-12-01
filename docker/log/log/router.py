#-*- coding: utf-8 -*-
# Creation Date : 2018-11-27
# Created by : Antoine LeBel
import json
from log import log, log_factory, nice_json
import datetime
import re
import json

class Router():
    """
    This has the same behavior as an api gateway.
    It route rabbitmq messages instead.
    """

    def route(self, req):
        try:
            req_dict = json.loads(req)
        except:
            print("Could not route request")
            #TODO build a standard error passing structure
            return "Error"

        return self._route(req)

    def _route(self, req):
        print("Looking for service : " + req.service)

        if req["service"] == "/log":
            return self.get(req)

        if req["service"] == "/log/date":
            return self.api_id(self, req)

    def get(self, req):
        log_name = req.args['type']
        behavior = req.args['behavior']

        factory = log_factory.LogFactory()
        log = factory.create_log(log_name, behavior)
        logs = log.fetch_log()
        return nice_json(logs)

    def api_id(self, req):
        log_name = req.args['type']
        behavior = req.args['behavior']

        if not self.is_log_type(log_name):
            return "Error: Incorrect log type, should be syslog or statlog"

        if not self.is_behavior(behavior):
            return "Error: Incorrect behavior, should be text or graph"

        factory = log_factory.LogFactory()
        log = factory.create_log(log_name, behavior)
        db = log.fetch_log()

        if 'date' in req.args:
            laDate = req.args['date']
            if not self.is_valid_date(laDate):
                return "Error: Invalid date format, should be YYYY-MM-DD"
        else:
            return "Error: No date field provided. Please specify an date."
        if laDate not in db:
            return "Error : date provide not found in the db."

        return nice_json(db[laDate])

    def is_valid_date(une_date):
        try:
            datetime.datetime.strptime(une_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def is_behavior(self, behavior):
        liste = ["text", "graph"]
        return behavior in liste

    def is_log_type(self, log_name):
        liste = ["syslog", "statlog"]
        return log_name in liste
