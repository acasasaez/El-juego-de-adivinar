# El-juego-de-adivinar

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/acasasaez/El-juego-de-adivinar-2.0.git)
https://github.com/acasasaez/El-juego-de-adivinar-2.0.git

Hemos resuelto un juego de adivinar con valores enteros entre 0 y 99.
El diagrama de flujo que tenemos en nuestro código es el siguiente:

![diagrama de flujo adivine el número](/acasasaez/El-juego-de-adivinar-2.0/figmafoto.png)

```importar aleatoriamente
numero = aleatorio. randint(0,99)
intento = int (input ("Elige un número del 0 al 99: "))
numero_intento= 0
while intento != numero_intento:
    si intento < numero:
        print ("Demasiado pequeño")
        numero_intento = numero_intento + 1
        intento = int (input ("Elige un número del 0 al 99: "))
    si intento > numero:
        imprimir ("Demasiado grande")
        número_intento = número_intento + 1
        intento = int (input ("Elige un número del 0 al 99: "))
    if numero == intento:
        print ("Enhorabuena, has acertado") 
        número_intento = número_intento + 1
        print ("Número de intentos:" + str(número_intento))```
