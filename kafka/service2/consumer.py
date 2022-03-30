from kafka import KafkaConsumer

from settings import kafka_settings

consumer = KafkaConsumer(
    'events',
    bootstrap_servers=[kafka_settings.url],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode(),
)


def main():
    for msg in consumer:
        print(msg.value)


if __name__ == '__main__':
    main()
