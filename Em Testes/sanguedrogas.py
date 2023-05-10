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

def desvio ():
    difD = dD - 200
    velE = vb + kpd*difD
    velD = vb - kpd*difD
    left_motor.run(velE)
    right_motor.run(velD)

def seglinha ():
    difL = vE - vD
    velE = vb + kpl*difL
    velD = vb - kpl*difL
    left_motor.run(velE)
    right_motor.run(velD)

while True:

    dF = ultraF.distance()
    dD = ultraD.distance()

    vD = cor_dir.reflection()
    vE = cor_esq.reflection()

    if dF <= 200:
        desvio()
    else:
        seglinha()
    