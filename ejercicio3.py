#FUNCION Para saber si un Año bisiesto

def año(dias):
      if days % 4 == 0:
          print("El año es bisiesto")
      elif days % 100 == 0:
          print("El año es bisiesto")
      elif days % 400 == 0:
          print("El año es bisiesto")   
      else:
          print("El Año no es bisiesto")


days = int(input("Introduzca el Año: "))
año(days)



