#-*- coding: utf-8 -*-
# Creation Date : 2018-11-20
# Created by : Antoine LeBel
import pika
import sys

class Receiver():
    def __init__(self, host, queue, port):
        self.host = host
        self.queue = queue
        self.port = port

        self._get_ready()
        #TODO
        # self.router = router.Router()

    def _get_ready(self):
        self.connection = self._connection()
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
        self._prepare_consume()

    def _prepare_consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.on_request, queue=self.queue)

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
        #CALL SERGE LOG SERVICE HERE
        print("Received " + str(body))
        result = str(body) + "aaaaaa"

        #Return to sender on temporary queue (reply_to)
        ch.basic_publish(exchange="",
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = props.correlation_id),
                        body = result)

        #Acknownledge to public queue that the message has been processed
        ch.basic_ack(delivery_tag = method.delivery_tag)
