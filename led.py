import RPi.GPIO as GPIO
from time import sleep

RED_PIN = 12
GREEN_PIN = 16
BLUE_PIN = 18

CLK_PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

COLORS = ['red', 'blue', 'green', 'white', 'yellow', 'cyan', 'magenta']


def blink(pin):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def turn_off(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def red_on():
    blink(RED_PIN)


def red_off():
    turn_off(RED_PIN)


def green_on():
    blink(GREEN_PIN)


def green_off():
    turn_off(GREEN_PIN)


def blue_on():
    blink(BLUE_PIN)


def blue_off():
    turn_off(BLUE_PIN)


def yellow_on():
    blink(RED_PIN)
    blink(GREEN_PIN)


def yellow_off():
    turn_off(RED_PIN)
    turn_off(GREEN_PIN)


def cyan_on():
    blink(GREEN_PIN)
    blink(BLUE_PIN)


def cyan_off():
    turn_off(GREEN_PIN)
    turn_off(BLUE_PIN)


def magenta_on():
    blink(RED_PIN)
    blink(BLUE_PIN)


def magenta_off():
    turn_off(RED_PIN)
    turn_off(BLUE_PIN)


def white_on():
    blink(RED_PIN)
    blink(GREEN_PIN)
    blink(BLUE_PIN)


def white_off():
    turn_off(RED_PIN)
    turn_off(GREEN_PIN)
    turn_off(BLUE_PIN)


current_color_idx = 0
clk_last_state = GPIO.input(CLK_PIN)

try:
    while True:
        clk_state = GPIO.input(CLK_PIN)
        if clk_last_state == clk_state:
            continue

        off_color_func = globals()[f'{COLORS[current_color_idx]}_off']
        off_color_func()

        current_color_idx = (current_color_idx + 1) % len(COLORS)

        on_color_func = globals()[f'{COLORS[current_color_idx]}_on']
        on_color_func()

        clk_last_state = clk_state

        sleep(0.01)
finally:
    GPIO.cleanup()
