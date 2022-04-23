import random
import time
from typing import Any

import RPi.GPIO as GPIO
from paho.mqtt import client as mqtt_client
from pirc522 import RFID
from pydantic import BaseModel

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rc522 = RFID()


BROKER = 'broker.hivemq.com'
PORT = 1883
TOPIC = 'vkm/arkhipov/events'
CLIENT_ID = f'python-mqtt-{random.randint(0, 1000)}'


class Event(BaseModel):
    sensor_id: int
    type_sensor: str
    type_value: str
    value: Any


def connect_mqtt():
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


def publish(client):
    while True:
        rc522.wait_for_tag()
        error, tag_type = rc522.request()

        if error:
            continue

        error, uid = rc522.anticoll()

        if error:
            continue

        event = Event(
            sensor_id=1,
            type_sensor='rfid',
            type_value='1',
            value=uid,
        )
        event_msg = event.json()

        client.publish(TOPIC, event.json())
        print('Событие {} отправлено'.format(event_msg))

        time.sleep(1)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    try:
        run()
    finally:
        GPIO.cleanup()
