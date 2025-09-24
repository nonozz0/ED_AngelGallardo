# Bubble Sort vs `sorted()` en Python

Este programa compara el algoritmo Bubble Sort con la función incorporada `sorted()` de Python.


## Funcionamiento
- Bubble Sort: recorre la lista varias veces, intercambiando pares de elementos hasta que quedan ordenados. Es sencillo de entender, pero muy ineficiente en listas grandes (complejidad O(n²)).  
- sorted(): utiliza algoritmos mucho más optimizados (Timsort), rápidos incluso con grandes cantidades de datos.


## Pruebas realizadas
1. Evaluación por tamaño: se mide el tiempo en listas de 100, 500, 1000, 5000 y 10000 elementos.  
   - Bubble Sort es muy lento en comparación con `sorted()`.  
   - Se calcula también la relación entre ambos tiempos.  

2. Casos específicos: se prueban listas:  
   - Totalmente ordenada.  
   - En orden inverso.  
   - Casi ordenada.  


## Resultados esperados
- `sorted()` siempre supera por mucho a Bubble Sort.  
- En listas ya ordenadas, Bubble Sort mejora un poco, pero sigue siendo muy inferior.  
- Para listas grandes, la diferencia de tiempo es enorme.


## Conclusión
Bubble Sort es útil solo como ejemplo académico de algoritmos básicos, pero no debe usarse en la práctica.  
La función `sorted()` es la opción correcta en Python por su eficiencia y optimización.
