#-*- coding: utf-8 -*-
# Creation Date : 2018-11-20
# Created by : Antoine LeBel
import pika
import uuid
import codecs
import logging
import sys
import socket

class Receiver():
    TIMEOUT = 10 #second

    def __init__(self, host, queue, port):
        self.host = host
        self.queue = queue
        self.port = port

        self.connection = self._connection()
        self.channel = self.connection.channel()

        #TODO
        # self.router = router.Router()

    def _prepare_consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.on_request, queue=self.queue)
        self.channel.queue_declare(queue=self.queue)

    def _connection(self):
        try:
            connection = pika.ConnectionParameters(host=self.host, port=self.port)
            return pika.BlockingConnection(connection)
        except Exception as e:
            # TODO manage errors
            print("something wrong with pika connection")
            sys.exit(1)

    def consume(self):
        print("Starting log receiver")
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        #TODO
        print("Received " + body)
        result = body + "aaaaaa"
        ch.basic_publish(exchange="",
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = props.correlation_id),
                        body = result)

        ch.basic_ack(delivery_tag = method.delivery_tag)

    def _on_timeout(self):
        msg = "Client time out"
        print(msg)
        self.connection.close()
        raise Exception(msg)

    @staticmethod
    def is_service_available():
        """
        Checks if rabbitmq is listening.
        """
        port = config.get("rabbit", "port")
        host = config.get("rabbit", "host")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))

        if result == 0:
            return True
        else :
            return False
