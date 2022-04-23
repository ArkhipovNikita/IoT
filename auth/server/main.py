import random
from enum import Enum
from typing import Any

from db import create_login, has_uid_access
from paho.mqtt import client as mqtt_client
from pydantic import BaseModel

BROKER = 'broker.hivemq.com'
PORT = 1883
EVENT_TOPIC = 'vkm/arkhipov/events'
COMMAND_TOPIC = 'vkm/arkhipov/commands'
CLIENT_ID = f'python-mqtt-{random.randint(0, 100)}'


class MessageType(Enum):
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'


class Command(BaseModel):
    sensor_id: int
    type_sensor: str
    type_value: str
    type_message: MessageType
    value: Any


class Event(BaseModel):
    sensor_id: int
    type_sensor: str
    type_value: str
    value: Any


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        event = Event.parse_raw(msg.payload)

        type_message = MessageType.SUCCESS if has_uid_access(event.value) else MessageType.ERROR
        command = Command(
            sensor_id=2,
            type_sensor='passive_buzzer',
            type_value='1',
            type_message=type_message,
            value='1',
        )

        client.publish(COMMAND_TOPIC, command.json())

        create_login(event.value)

    client.subscribe(EVENT_TOPIC)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
