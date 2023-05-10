#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

valor1 = 250 #velocidade maxima
valor2 = 50 #velocidade minimia

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

ultraF = UltrasonicSensor(Port.S1)
ultraD = UltrasonicSensor(Port.S4)

cor_dir = ColorSensor(Port.S2)
cor_esq = ColorSensor(Port.S3)

distF = int(ultraF.distance())/10
distD = int(ultraD.distance())/10

vel_direito = 0
vel_esquerdo = 0

def desvio():
    while True:
        KpD = 1.5
        VbD = 80
    
        corE = cor_esq.reflection()
        corD = cor_dir.reflection()

        if corE <= 10 or corD <=10:
            break

        SensorD = ultraD.distance()

        if SensorD < 200:

            erroD = (SensorD/10) - 15
            VelED = VbD + KpD * erroD
            VelDD = VbD - KpD * erroD

            right_motor.run(VelDD)
            left_motor.run(VelED)
    
        else:
            right_motor.run(60)
            left_motor.run(100)

        wait(15)

desvio()