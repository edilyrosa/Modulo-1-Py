
# ***************Los operadores lógicos en Python (and, or, not) 
# se utilizan para "combinar expresiones booleanas" (que son True o False). 
# Permiten la tomar decisiones basadas en varias condiciones al mismo tiempo.

# ***************Operador and (Y lógico):
# Devuelve True sólo si "ambas" condiciones son verdaderas.
# Si alguna es False, el resultado es False.

# ***************Operador or (O lógico):
# Devuelve True si "al menos una" condición es verdadera.
# Sólo devuelve False si todas las condiciones son falsas.

# ***************Operador not (Negación lógica):
# Invierte el valor booleano de una condición.
# Si la condición es True, not la convierte en False, y viceversa.

print('Operadores Logicos')
print('True and False =', True and False) #True and False = False
print('True or False =', True or False) #True or False = True
print('not False =', not False) #not False = True

verdadero = True
falso = False
print(verdadero and verdadero)
print(verdadero and False) 
print( not verdadero) #...


print('ejercicios')
temperatura = 20
hace_sol = True
if temperatura > 20 and hace_sol: #* ambas deben ser TRUE
    print("¡Día perfecto para un picnic!")
else:
    print("Mejor quedarnos en casa.")
# El mensaje se imprime sólo si la temperatura es mayor que 20 y está soleado.

tiene_paraguas = False
if hace_sol or tiene_paraguas:  #* al menos 1 debe ser TRUE
    print("¡Vamos a pasear!")
else:
    print("Mejor quedarnos en casa.")
# Aquí se sale a pasear si hace sol o si se tiene paraguas.


#& ⛹🏽⛹🏽⛹🏽⛹🏽 EJERCICIO 1: como puedo expresar que: si es NO hace_sol deberia quedarme en casa
if not hace_sol:
    print("Quizás deberíamos quedarnos en 🏠.")
else:
    print("Debo salir, hay 🌞.")
# Se imprime sólo si no está soleado.