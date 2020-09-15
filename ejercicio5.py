# ejercicio palindromico

def numero_palindromo():
     num1 = int(input("Digite un Numero: "))
     num2 = int(input("Digite otro Numero: "))
     num3 = num1 * num2

     #el resultado del numero lo convertimos a STR, para hacer la compraracion si es palindromo.
     palindromo = str(num3)
     #Con esta variable recorremos el resultado desde la derecha a izquierda.
     reverso = palindromo[::-1]

     #aqui comparamos el resultado original, con la variabble que tiene el resultado opuesto.
     if palindromo == reverso:
         print("El numero es un Palindromo")
    
     else:
          print("El numero no es un Palindromo")

numero_palindromo()
