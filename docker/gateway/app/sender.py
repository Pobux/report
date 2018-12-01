#-*- coding: utf-8 -*-
# Creation Date : 2018-11-11
# Created by : Antoine LeBel
import pika
import uuid
import codecs
import logging
import sys
import socket

class Sender():
    TIMEOUT = 10 #second

    def __init__(self, host, queue, port):
        self.host = host
        self.queue = queue
        self.port = port

        self.connection = self._connection()
        self.channel = self.connection.channel()
        self.callback_queue = None
        self.corr_id = None

    def send(self, body):
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                  queue=self.callback_queue)

        self.connection.add_timeout(self.TIMEOUT, self._on_timeout)

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange = "",
                                   routing_key = self.queue,
                                   properties = pika.BasicProperties(
                                       reply_to = self.callback_queue,
                                       correlation_id = self.corr_id
                                   ),
                                   body = body)

    def manage_response(self):
        try:
            while self.response is None:
                self.connection.process_data_events()
            return self.response
        except pika.exceptions.ConnectionClosed:
            print("Connection closed.")
            sys.exit(1)
        pass

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def _connection(self):
        try:
            connection = pika.ConnectionParameters(host=self.host, port=self.port)
            return pika.BlockingConnection(connection)
        except Exception as e:
            print(e)
            print("something wrong with pika connection")
            sys.exit(1)

    def _on_timeout(self):
        msg = "Client time out"
        print(msg)
        self.connection.close()
        raise Exception(msg)
