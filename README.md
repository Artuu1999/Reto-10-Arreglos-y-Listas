# Reto #10 Arreglos y Listas
Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando lo aprendido acerca de los arreglos y listas dentro de nuestra clase de programación de computadores.

## Ejemplo No. 1
Diseñar un código, el cual al ejecutarlo calcule el promedio de un arreglo de números reales.
El siguiente código, es la solución al problema descrito anteriormente:
```sh
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
```
Así se ve el programa funcionando:

![image](https://github.com/Artuu1999/algoritmos-reto-4/assets/124615034/0a168d77-c59d-4d91-8e7b-0c5e0be309a2)

## Ejemplo No. 2
Al haber dos arreglos de igual tamaño, crear un código que determine el producto punto de números reales.
El código solución al ejemplo es el siguiente:
```sh
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
```
Programa funcionando:

![image](https://github.com/Artuu1999/algoritmos-reto-4/assets/124615034/d5a7a957-9498-42f4-b2a4-d2f5243c6ea2)

## Ejemplo No. 3
Diseñar un programa en Python que ubique al final del arreglo todos los ceros que aparezcan en dicho arreglo.
A continuación la solución a dicho problema:
```sh
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
```
Así se ve el programa funcionando:

![image](https://github.com/Artuu1999/algoritmos-reto-4/assets/124615034/eb4c93b9-48d2-4179-bcfc-fe3d58870af9)

## Sorting
Traducido al español, significa ordenamiento, dentro del argot de la programción es  el proceso de organizar elementos según una característica de estos, ya sea según su valor númerico, alfabético, fecha, entre otros.

## Bubble-sort
En programación se puede definir como un algoritmo que se basa en comparar elementos de un arreglo, comenzando con el primero con el segundo, luego el segundo con el tercero y así sucesivamente, determinando si los elementos están dentro de la posición correcta.

## FIN
Hasta acá llega nuestro camino en el presente repo, espero que haya sido de tu interés, si encuentras algún error o alguna inconsistencia, no dudes en contactarme y hacermela saber.
Muchas Gracias por tu atención.

   **"El coraje es solo una acumulación de pequeños pasos."**
         - George Konrad
