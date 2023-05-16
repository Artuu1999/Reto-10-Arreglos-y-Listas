#Se define la función de la lista
def Arreglo(n) -> list:
    lista = [] #Se crea una lista vacía
    for i in range(n): #Ciclo for para ingresar cada elemento
        elemento = float(input("Ingrese el elemento que contendrá el arreglo: "))
        lista.append(elemento) #Se agregan los elementos ingresados a la lista
    return lista #Se retorna la lista

#Función para hallar el promedio
def promedioArreglo(lista) -> float:
    promedio = 0 #Se inicializa
    for elemento in lista:  #Ciclo for para cada elemento de la lista
        promedio += elemento  #Se actualiza
    promedio = promedio / len(lista) #Se divide la suma de elemento entre la cantidad total de elementos
    return promedio 

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de elementos que tendrá la lista: ")) #Cantidad de elementos que tendrá la lista
    #Se llaman las funciones definidas anteriormente
    lista = Arreglo(n)
    media = promedioArreglo(lista)
    #Se imprime la lista y el promedio de esta
    print("La lista ingresada anteriormente es: ", lista)
    print("El promedio de la lista ingresada es: ",media)