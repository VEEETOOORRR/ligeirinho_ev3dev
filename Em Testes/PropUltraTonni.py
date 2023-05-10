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
    valor1 = 250
    valor2 = 50

    a = (valor1 - valor2)/73
    b = valor1 - (76 * a)


    valorEsquerdo = (corE.reflection())
    valorDireito = (corD.reflection())

    vel_direito = a*valorDireito + b
    vel_esquerdo = a*valorEsquerdo + b

    motorD.run(vel_direito)
    motorE.run(vel_esquerdo)

def DesviarObstaculo():
    while (corD.reflection() > 10 and corE.reflection() > 10):
        KpD = 1.5
        VbD = 80
        erroD = 0

        SensorD = ultraD.distance()

        if SensorD < 200:

            erroD = (SensorD/10) - 10
            VelED = VbD + KpD * erroD
            VelDD = VbD - KpD * erroD

            motorD.run(VelDD)
            motorE.run(VelED)
    
        else:

            motorD.run(60)
            motorE.run(100)
        
        valorEsquerdo = (corE.reflection())
        valorDireito = (corD.reflection())
        
def Baliza():
    


while True:
    SensorF = ultraF.distance()

    if SensorF <= 150:
        Ajustar()
        DesviarObstaculo()
        Baliza()

    else:
        SeguirLinha()




    