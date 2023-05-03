#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

seguirLinha = True
desvio = False

erro = valorDesD = valorDesF= 0
Vb = 150
Kp = 4
comp = 40       

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.D)

corE = ColorSensor(Port.S3)
corD = ColorSensor(Port.S2)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4)

while True:

    motorD.run(0)
    motorE.run(0)

    while (seguirLinha == True) and (desvio == False):

        valor_esq = int(corE.reflection())
        valor_dir = int(corD.reflection())

        distF = ultraF.distance()

        if distF <= 200:
            seguirLinha  = False
            desvio       = True

        erro = (valor_esq - valor_dir) + 10

        mE = Vb + Kp*erro
        mD = Vb - Kp*erro

        motorD.run(mD+comp)
        motorE.run(mE)
        
    motorD.run(0)
    motorE.run(0)

    while (seguirLinha == False) and (desvio == True):

        distF = ultraF.distance()
        distD = ultraD.distance()

        print(distD)
        print(distF)

        wait(1000)