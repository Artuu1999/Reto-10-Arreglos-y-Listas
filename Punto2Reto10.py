#Se define la función de la lista
def arreglo1(n) -> list:
    lista1 = [] #Se crea una lista vacía
    for i in range(n): #Ciclo for para ingresar cada elemento
        elemento = int(input("Ingrese el elemento que contendrá el primer arreglo: "))
        lista1.append(elemento) #Se agregan los elementos ingresados a la lista
    return lista1 #Se retorna la lista

#Se define la función de la lista
def arreglo2(n) -> list:
    lista2 = [] #Se crea una lista vacía
    for i in range(n): #Ciclo for para ingresar cada elemento
        elemento = int(input("Ingrese el elemento que contendrá el segundo arreglo: "))
        lista2.append(elemento) #Se agregan los elementos ingresados a la lista
    return lista2 #Se retorna la lista

#Función para hallar el producto punto
def productoPunto (lista1, lista2) -> int:
    producto = 0 #Se inicializa
    for i in range (n):  #Ciclo for para iterar sobre cada elemento
        producto = producto + lista1[i]*lista2[i] #Se halla el producto punto entre ambas listas
    return producto #Se retorna la función


if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de elemento que tendrá los dos arreglos
    n = int(input("Ingrese la cantidad de elementos que tendrán las dos listas: "))
    #Se llaman las funciones definidas anteriormente
    lista1 = arreglo1(n)
    lista2 = arreglo2(n)
    Producto = productoPunto(lista1, lista2)
    #Se imprime la lista y el producto punto de esta
    print("La primer lista ingresada anteriormente es: ", lista1)
    print("La segunda lista ingresada anteriormente es: ", lista2)
    print("El producto punto de las dos listas es: ", Producto)