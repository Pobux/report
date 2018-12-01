#-*- coding: utf-8 -*-
# Creation Date : 2018-11-24
# Created by : Antoine LeBel
from log import receiver

messenger = receiver.Receiver("rabbit", "log_queue", 5672)
messenger.consume()
