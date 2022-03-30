from settings import kafka_settings

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=kafka_settings.url)


def send_event(message: str):
    producer.send('events', value=message.encode())
