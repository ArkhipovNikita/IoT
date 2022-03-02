import random
import time

import RPi.GPIO as GPIO
from paho.mqtt import client as mqtt_client

CLK_PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BROKER = 'broker.hivemq.com'
PORT = 1883
TOPIC = "vkm/arkhipov"
CLIENT_ID = f'python-mqtt-{random.randint(0, 1000)}'


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
    clk_last_state = GPIO.input(CLK_PIN)

    while True:
        clk_state = GPIO.input(CLK_PIN)
        if clk_last_state == clk_state:
            continue

        msg = f'Кнопка нажата, состояние {clk_state}'
        result = client.publish(TOPIC, msg)
        print(msg)

        clk_last_state = clk_state
        time.sleep(0.01)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    try:
        run()
    finally:
        GPIO.cleanup()
