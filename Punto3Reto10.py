#Se define la función de la lista
def arreglo(n) -> list:
    lista = [] #Se crea una lista vacía
    for i in range(n): #Ciclo for para ingresar cada elemento
        elemento = int(input("Ingrese el elemento que contendrá el arreglo: "))
        lista.append(elemento) #Se agregan los elementos ingresados a la lista
    return lista #Se retorna la lista

#Función para modificar la lista
def arregloCerosFinal (lista):
    for i in lista:  #Bucle para iterar sobre cada elemento de la lista
        if i == 0:  #Condicional por si el elemento es 0
            lista.remove(i) #Remover el elemento de la lista
            lista.append(i) #Agregarlo de nuevo, se agrega al final de la lista
    return lista #Se retorna la lista
        
if __name__ == "__main__":
    #Se solicita el ingreso de la cantidad de elementos que tendrá el arreglo
    n = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))
    lista = arreglo(n) #Se llama la función de la lista original
    print("La lista ingresada anteriormente es: ", lista) #Se imprime la lista original
    listaCeros = arregloCerosFinal(lista) #Se llama la función de la lista modificada
    print("La lista con los ceros al final es la siguiente: ", listaCeros) #Se imprime dicha lista