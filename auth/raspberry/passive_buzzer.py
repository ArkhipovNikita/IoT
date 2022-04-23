import random
import time
from enum import Enum
from itertools import repeat
from typing import Any

import RPi.GPIO as GPIO
from paho.mqtt import client as mqtt_client
from pydantic import BaseModel

GPIO.setmode(GPIO.BCM)

GPIO_PIN = 18
GPIO.setup(GPIO_PIN, GPIO.OUT)

Buzz = GPIO.PWM(GPIO_PIN, 50)


BROKER = 'broker.hivemq.com'
PORT = 1883
TOPIC = 'vkm/arkhipov/commands'
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


def play_success():
    Buzz.ChangeFrequency(50)

    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()


def play_error():
    Buzz.ChangeFrequency(100)

    for _ in repeat(None, 2):
        Buzz.start(50)
        time.sleep(0.7)
        Buzz.stop()
        time.sleep(0.5)


ACTIONS = {
    MessageType.SUCCESS: play_success,
    MessageType.ERROR: play_error,
}


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
        command = Command.parse_raw(msg.payload)

        action = ACTIONS[command.type_message]
        action()

    client.subscribe(TOPIC)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    try:
        run()
    finally:
        GPIO.cleanup()
