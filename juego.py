import random
numero = random.randint(0,99)
intento = int (input ("Elige un número del 0 al 99: "))
número_intento= 0
while intento != número_intento:
    if intento < numero:
        print ("Demasiado pequeño")
        número_intento = número_intento + 1
        intento = int (input ("Elige un número del 0 al 99: "))
