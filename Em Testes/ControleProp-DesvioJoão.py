#!/usr/bin/env pybricks-micropython

# Autor: João

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

motorE = Motor(Port.B)
motorD = Motor(Port.D)

CorD = ColorSensor(Port.S3)
CorE = ColorSensor(Port.S2)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4) 

# =========================================== Funções Gerais ==========================================

def SeguirLinha():
    erro = VelE = VelD = 0
    Vb = 150
    Kp = 4

    valor_esq = CorE.reflection()
    valor_dir = CorD.reflection()

    erro = valor_esq - valor_dir
    VelE = Vb + Kp * erro
    VelD = Vb - Kp * erro

    motorD.run(VelD)
    motorE.run(VelE)

def Reajustar():
    motorE.run(0)
    motorD.run(0)
    wait(20)
    while True:
        valor_esq = CorE.reflection()
        motorD.run(100)
        if valor_esq <= 25:
            motorD.run(0)
            break

def DesvioProp ():
    while True:
        KpD = 3
        VbD = 150

        SenD = int(ultraD.distance())

        ErroD = SenD - 80

        print(ErroD)

        if (ErroD >= -10) and (ErroD <= 10):
            motorD.run(VbD + KpD * ErroD)
            motorE.run(VbD - KpD * ErroD)
        else:
            motorD.run(VbD - 50)
            motorE.run(VbD)
            
# ======================================== Giros ==================================================

def GirarE ():
    motorE.run(-100)
    motorD.run(100)
    wait(1850)
    motorE.stop()
    motorD.stop()

def GirarD ():
    motorE.run(100)
    motorD.run(-100)
    wait(1850)
    motorE.stop()
    motorD.stop()

# ==================================== Repetição de ações ======================================

while True:
    SensorFrontal = ultraF.distance()

    if SensorFrontal <= 122:
        GirarE()
        DesvioProp()
        break
    else:
        SeguirLinha()
