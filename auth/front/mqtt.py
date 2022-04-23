import random
from enum import Enum
from typing import Any

from paho.mqtt import client as mqtt_client
from pydantic import BaseModel

BROKER = 'broker.hivemq.com'
PORT = 1883
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


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)

    return client


def beep(client: mqtt_client):
    command = Command(
        sensor_id=2,
        type_sensor='passive_buzzer',
        type_value='1',
        type_message=MessageType.ERROR,
        value='1',
    )

    client.publish(COMMAND_TOPIC, command.json())


client = connect_mqtt()
