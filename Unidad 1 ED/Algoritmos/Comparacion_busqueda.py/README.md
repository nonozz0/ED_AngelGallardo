# Búsqueda Lineal vs Búsqueda Binaria en Python

Este programa compara dos formas de buscar un elemento dentro de una lista: lineal y binaria.

## Funcionamiento
- Búsqueda lineal: recorre la lista elemento por elemento hasta encontrar el objetivo o llegar al final. Su complejidad es O(n).  
- Búsqueda binaria: funciona en listas ordenadas. Divide el rango a la mitad en cada paso, reduciendo rápidamente las posibilidades. Su complejidad es O(log n).  


## Experimento
Se prueba en listas de distintos tamaños: 1000, 10000, 50000 y 100000 elementos.  
Para cada lista:  
- Se buscan 5 elementos que sí están y 5 que no.  
- Se mide el tiempo promedio de búsqueda con ambos métodos.  
- Se calcula el ratio entre el tiempo de búsqueda lineal y binaria.  


## Resultados esperados
- La búsqueda lineal se vuelve muy lenta en listas grandes.  
- La búsqueda binaria mantiene tiempos muy bajos incluso con muchos elementos.  
- El ratio muestra que la búsqueda binaria es varias veces más rápida.  


## Conclusión
La búsqueda lineal es sencilla y funciona en cualquier lista, pero es poco eficiente.  
La búsqueda binaria, aunque requiere listas ordenadas, es la opción ideal para manejar grandes volúmenes de datos.
