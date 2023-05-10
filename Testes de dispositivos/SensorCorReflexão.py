#!/usr/bin/env pybricks-micropython

# Autor: João

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

corE = ColorSensor(Port.S3)
corD = ColorSensor(Port.S2)

while True:
    SensorEsquerdo = int(corE.reflection())
    SensorDireito = int(corD.reflection())

    print("Esquerdo:")
    print(SensorEsquerdo)
    print("Direito:")
    print(SensorDireito)

    wait(500)