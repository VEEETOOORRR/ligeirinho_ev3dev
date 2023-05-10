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

def Ajustar():
    while True:
        SensorD = int(ultraD.distance())
        motorE.run(-60)
        motorD.run(60)
        if SensorD <= 200:
            break
    pass

def SeguirLinha():
    erro = VelE = VelD = 0
    Vb = 150
    Kp = 4
    comp = 40

    valor_esq = corE.reflection()
    valor_dir = corD.reflection()

    erro = valor_esq - valor_dir
    VelE = Vb - Kp * erro
    VelD = Vb + Kp * erro

    motorD.run(VelD)
    motorE.run(VelE)

def DesviarObstaculo():
    while True:
        KpD = 1.5
        VbD = 80
        erroD = 0
    
        SensorD = ultraD.distance()

        if SensorD < 200:

            erroD = (SensorD/10) - 15
            VelED = VbD + KpD * erroD
            VelDD = VbD - KpD * erroD

            motorD.run(VelDD)
            motorE.run(VelED)
    
        else:

            motorD.run(60)
            motorE.run(100)

        wait(15)

while True:
    SensorF = ultraF.distance()

    if SensorF <= 200:
        Ajustar()
        DesviarObstaculo()
    else:
        SeguirLinha()


    