#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

valor1 = 250
valor2 = 50

a = (valor1 - valor2)/73
b = valor1 - (76 * a)

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)

while True:

    valorEsquerdo = (cor_esq.reflection())
    valorDireito = (cor_dir.reflection())

    vel_direito = a*valorDireito + b
    vel_esquerdo = a*valorEsquerdo + b

    right_motor.run(vel_direito)
    left_motor.run(vel_esquerdo)