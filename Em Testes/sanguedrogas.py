#!/usr/bin/env pybricks-micropython

#Vinicius

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

kpd = 7
kpl = 4
vb = 157

left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)

def linha():
    distF = ultraF.distance()
    while distF > 200:
        distF = ultraF.distance()
        refD = cor_dir.reflection()
        refE = cor_esq.reflection()
        dif = refD - refE

        velD = vb + kpl*dif
        velE = vb - kpl*dif

        left_motor.run(velE)
        right_motor.run(velD)

linha()
