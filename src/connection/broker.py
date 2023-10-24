import json
import pika
import logging

from src.config.global_config import app_setting

connected_clients = set()

logger = logging.getLogger()

class BrokerHelper:
    EXCHANGE = app_setting.RABBIT_EXCHANGE
    ROUTING_KEY = app_setting.RABBIT_ROUTING
    QUEUE = app_setting.RABBIT_QUEUE

    def __init__(self) -> None:
        credentials = pika.PlainCredentials(
            username=app_setting.RABBIT_USER,
            password=app_setting.RABBIT_PASS
        )
        param_public = pika.ConnectionParameters(
            host=app_setting.RABBIT_HOST,
            port=app_setting.RABBIT_PORT,
            virtual_host=app_setting.RABBIT_VHOST,
            credentials=credentials
        )
        self.__connection = pika.BlockingConnection(param_public)

    async def publish_message(self, message_body) -> None:
        credentials = pika.PlainCredentials(
            username=app_setting.RABBIT_USER,
            password=app_setting.RABBIT_PASS
        )
        param_public = pika.ConnectionParameters(
            host=app_setting.RABBIT_HOST,
            port=app_setting.RABBIT_PORT,
            virtual_host=app_setting.RABBIT_VHOST,
            credentials=credentials
        )
        conn_public = pika.BlockingConnection(parameters=param_public)
        channel_public = conn_public.channel()
        channel_public.basic_publish(
            exchange=self.EXCHANGE, routing_key=self.ROUTING_KEY, body=json.dumps(message_body)
        )
        channel_public.close()
        conn_public.close()

    async def consume_data(self):
        credentials = pika.PlainCredentials(username=app_setting.RABBIT_USER,
                                            password=app_setting.RABBIT_PASS)
        param_public = pika.ConnectionParameters(
            host=app_setting.RABBIT_HOST,
            port=app_setting.RABBIT_PORT,
            virtual_host=app_setting.RABBIT_VHOST,
            credentials=credentials
        )
        connection = pika.BlockingConnection(parameters=param_public)
        channel = connection.channel()

        result = channel.queue_declare(queue=self.QUEUE, durable=True)
        channel.queue_bind(result.method.queue, exchange=self.EXCHANGE, routing_key=self.ROUTING_KEY)

        method_frame, header_frame, body = channel.basic_get(queue=result.method.queue, auto_ack=True)

        if body is not None:
            return body

    async def close_connection(self) -> None:
        self.__connection.close()


broker = BrokerHelper()
