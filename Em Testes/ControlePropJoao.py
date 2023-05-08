#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.D)

corE = ColorSensor(Port.S3)
corD = ColorSensor(Port.S2)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4) 

def SegueLinhas ():
    while True:
        erro = 0
        Vb = 150
        Kp = 4
        comp = 40

        valor_esq = int(corE.reflection())
        valor_dir = int(corD.reflection())

        distF = ultraF.distance()

        if distF <= 200:
            break

        erro = (valor_esq - valor_dir) + 10

        mE = Vb + Kp*erro
        mD = Vb - Kp*erro

        motorD.run(mD+comp)
        motorE.run(mE)

def DesvioObstaculo ():
    while True:
        

SegueLinhas()