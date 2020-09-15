#hacer una funcion que reciba una cedula como argumento y diga si es valida o no


def identidad(ced):
     
     if len(cedula) == 11:
         print("Cedula valida")
         return True
     else:
         print("Cedula no valida")


cedula = input("Introduzca su cedula de identidad: ")
identidad(cedula)