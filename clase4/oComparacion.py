
# ***************Los operadores de Comparación en Python 
# permiten "comparar dos" valores o expresiones y siempre devuelven un 
# resultado booleano (True o False). Usados para tomar decisiones en un programa, 
# por ejemplo dentro de estructuras condicionales (if, while, etc.).
print('Operadores de Comparación: ==, !=, <, >, <=, >=')

#*************⁉️¿Cómo funcionan con tipo de dato numéricos?
# Es intuitivo, comparan sus valores numéricos naturalmente.
print(4 == 4.0)  # True, porque 4 y 4.0 representan el mismo valor numérico
print(4 >= 4.0)  # True, porque 4 y 4.0 representan el mismo valor numérico
print(5 > 3)     # True
print(5 > 5.0)   # False, son iguales.
print(5 != 5.0)  # False, son iguales.

#*************⁉️¿Cómo funcionan con tipo de dato Booleanos?
# Se tratan como 1 (True) y 0 (False).
print(True > False)  #* True (1 > 0)



# *************⁉️¿Cómo funcionan con tipo de dato String?
# ✅Se comparan lexicográficamente según el orden Unicode de cada carácter.
# Python compara cadena por cadena carácter a carácter: 
# 1. Python compara cadena 
print("hola" == "hola")  # True  
print("hola" != "mundo") # True 

# 2. Python compara carácter a carácter:
# usando el valor numérico Unicode de cada carácter (obtenible con ord(caracter)).
print(ord("A")) #65
print(ord("a")) #97
print("A" < "a") #* True, porque mayúsculas tienen "menor" código Unicode que las minúsculas 
#* 👀Entonces: Las letras mayúsculas y minúsculas se diferencian porque tienen 


#✅ La comparación se realiza en orden: se compara el primer carácter de ambas cadenas; 
# si son iguales, se pasa al siguiente, y así sucesivamente, hasta encontrar la diferencia que 
# devuelva el booleano resultado.
print(ord("a"), ord("b"), ord("c"), ord("d")) # 97 98 99 100
print("abc" < "abd")  #* True, porque 'c' es menor que 'd'  
print("Mark" > "Jack") # True, 'M' (77) > 'J' (74)
print("Mark" == "mark") # False, mayúsculas y minúsculas no son iguales


# ✅Puedes usar los operadores de comparacion "entre dos cadenas".
# 🚫No mezcles tipos diferentes, como str con int en comparaciones directas, porque no son compatibles, 
# si lo intentas usando operadores de orden (<, >, etc.), Python lanzará un TypeError. 
# Sin embargo, == y != sí pueden comparar distintos tipos siempre, retornando casi siempre False 
# (excepto casos especiales).
print("3" == 3)  # False  
#! print("3" < 3)   #* TypeError: '<' not supported between instances of 'str' and 'int'

# ®️🤯Resumen clave
# 👀Los operadores de comparación devuelven True o False.
# 👀Debes comparar preferentemente valores del mismo tipo para evitar errores.
# 👀Para cadenas, la comparación es lexicográfica, sensible a mayúsculas y minúsculas.
# 👀En tipos numéricos, se comportan naturalmente según valor.
# 👀== y != pueden comparar distintos tipos pero otros operadores NO.


print('"M" == 77', "M" == 77)           #*"M" == 77 False
print('ord("M") == 77', ord("M") == 77) #*ord("M") == 77 True