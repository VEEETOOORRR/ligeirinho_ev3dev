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
        motorE.run(-100)
        motorD.run(100)
        if SensorD <= 160:
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
    KpD = 2
    VbD = 80
    erroD = 0
    
    SensorD = int(ultraD.distance())

    erroD = (SensorD) - 150
    VelED = VbD + KpD * erroD
    VelDD = VbD - KpD * erroD

    motorD.run(VelDD)
    motorE.run(VelED)

while True:
    SensorF = ultraF.distance()

    if SensorF <= 200:
        Ajustar()
        DesviarObstaculo()
    else:
        SeguirLinha()


    