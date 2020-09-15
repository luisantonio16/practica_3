#Elevar un numero de X a Y
import math
def elevar():
     x = int(input("Digite un numero: "))
     y = int(input("Digite el numero al que desea elevar X: "))
     print("El " + str(x) + " elevado a "+ str(y) +" es: ", math.pow(x,y))


elevar()