
lista = [16, 29, 4, 21, 19]

def lista_numerica(list):
     # aqui imprimimos la lista original.
     print("Esta es la lista Original: " +str(lista))
     lista2 = []
     for elementos in lista:
         #aqui duplicamos la lista, se puede hacer, lista + lista o lista * 2.
         lista_new = elementos + elementos
         #aqui agregamos la lista ya duplicada a una lista vacia.
         lista2.append(lista_new)
     #imprimimos la lista duplicada    
     print("Esta es la lista Duplicada: "+str(lista2))
     
       
lista_numerica(list)    


