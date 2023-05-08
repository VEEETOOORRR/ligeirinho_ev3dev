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

def seglinha ():
    while True:
        difL = vE - vD
        velE = vb + kpl*difL
        velD = vb - kpl*difL
        left_motor.run(velE)
        right_motor.run(velD)
        if dF <= 200:
            break

def ajuste ():
    vE = cor_esq.reflection()
    vD = cor_dir.reflection()

    if vD <= 10:
        left_motor.run(-10)
        right_motor.run(40)
        if vD > 10 and vE > 10:
            seglinha()

def desvio ():
    left_motor.run(-100)
    right_motor.run(100)
    wait(50)
    while True:
        dD = ultraD.distance()

        vD = cor_dir.reflection()
        vE = cor_esq.reflection()

        difD = dD - 200
        velE = vb + kpd*difD
        velD = vb - kpd*difD
        left_motor.run(velE)
        right_motor.run(velD)

        if vD <= 10 or vE <= 10:
            ajuste()

while True:

    dF = ultraF.distance()
    dD = ultraD.distance()

    vD = cor_dir.reflection()
    vE = cor_esq.reflection()

    if dF <= 200:
        desvio()
    else:
        seglinha()
    