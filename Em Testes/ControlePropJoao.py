#!/usr/bin/env pybricks-micropython

# Autor: João

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.D)

# S3 = Direito
# S2 = Esquerdo

corE = ColorSensor(Port.S3) 
corD = ColorSensor(Port.S2)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4) 

def Reajustar():
    motorE.run(0)
    motorD.run(0)
    wait(20)
    while True:
        valor_esq = corE.reflection()
        motorD.run(100)
        if valor_esq <= 25:
            motorD.run(0)
            break
    pass

def Ajustar():
    while True:
        SensorD = int(ultraD.distance())
        motorE.run(-60)
        motorD.run(60)
        if SensorD <= 100:
            break
    pass

def SeguirLinha():
    erro = VelE = VelD = 0
    Vb = 180
    Kp = 4

    valor_esq = corE.reflection()
    valor_dir = corD.reflection()

    erro = valor_esq - valor_dir
    VelE = Vb - Kp * erro
    VelD = Vb + Kp * erro

    motorD.run(VelD)
    motorE.run(VelE)

def DesviarObstaculo():
    while True:
        KpD = 2
        VbD = 300
        erroD = 0

        valor_dir = corD.reflection()
        SensorD = ultraD.distance()

        erroD = SensorD - 100
        VelED = VbD + KpD * erroD
        VelDD = VbD - KpD * erroD

        motorD.run(VelDD)
        motorE.run(VelED)
 
        if (valor_dir <= 20):
            Reajustar()
            break
        
while True:
    SensorF = ultraF.distance()

    if SensorF <= 100:
        Ajustar()
        DesviarObstaculo()
    else:
        SeguirLinha()