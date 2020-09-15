"""hacer una funcion que reciba un valor inicial y uno final, imprimi las tablas de multiplicacion,
de los numeros multiplos de 6 que hay entre el valor inicial y final"""

def multiplicar(n1, n2):
     print("La Tabla de multiplicacion")
     for i in range(num1 , num2):
          print("6"+"x" + str(i) + "=" + str(i * 6))




num1 = int(input("Valor Inicial de la tabla: "))
num2 = int(input("Valor final de la tabla: "))
multiplicar(num1,num2)