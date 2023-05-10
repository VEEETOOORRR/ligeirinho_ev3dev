#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

b = 170
kp = 5

cor_dir = ColorSensor(Port.S3)
cor_esq = ColorSensor(Port.S2)

while True:

    valor_esq = cor_esq.reflection()
    valor_dir = cor_dir.reflection()
    dif = valor_esq - valor_dir

    vD = b + kp*dif
    vE = b - kp*dif
    left_motor.run(vE)
    right_motor.run(vD+100)

    

