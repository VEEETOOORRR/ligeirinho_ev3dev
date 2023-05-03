#!/usr/bin/env pybricks-micropython

#Vinicius

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

kp = 4
vb = 157

left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)


while True:

    distF = ultraF.distance()
    distD = ultraD.distance() 

    valorE = cor_esq.reflection()
    valorD = cor_dir.reflection()

    dif = valorE - valorD

    if distF <= 120 and distD >= 150:
        while True:
            if distD <= 150:
                right_motor.run(100)
                left_motor.run(100)
                wait(150)
                break
            else:
                distD = ultraD.distance()
                right_motor.run(-150)
                left_motor.run(150)
                break
            

    else:
        vel_direito = vb - kp*dif
        vel_esquerdo = vb + kp*dif 

        right_motor.run(vel_direito)
        left_motor.run(vel_esquerdo)