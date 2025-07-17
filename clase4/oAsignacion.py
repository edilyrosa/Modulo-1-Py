# # ***************Los operadores de Asignación en Python 
# Sirven para asignar valores a variables y actualizar esos valores. 
# El operador básico es =, que asigna directamente un valor, pero existen operadores compuestos 
# que combinan una operación con la asignación.

# *****************Operador básico de asignación
# = asigna el valor de la derecha a la variable de la izquierda.
# x = 7  # x recibe el valor 7


# ******************Operadores de asignación compuestos
# Permiten realizar una operación con el valor actual de la variable y luego 
# asignar el resultado a esa misma variable. Son equivalentes a escribir la operación completa 
# con asignación, pero en forma abreviada.

# ®️Resumen
# ✅El operador = asigna un valor directamente.
# ✅👀🤯Los operadores compuestos (+=, -=, *=, etc.) modifican la variable basándose en su valor actual.
# ✅Son útiles para escribir código más limpio y eficiente.

x = 5
x += 5
x -= 2
x *= 10
x /= 2
x //= 4
x %= 4
print("x es = ", (x)) #* x es =  2.0
x **= 0               #* Resultado 1.0
print("Resultado", (x)) 



print('Ejercicios')
a = 7
b = 2

x = a
x += b      #* x = x + 2 = 9
print('x += b:', x)

x = a
x -= b      #* x = x - 2 = 5
print('x -= b:', x)

x = a
x *= b      #* x = x * 2 = 14
print('x *= b:', x)

x = a
x /= b      #* x = x / 2 = 3.5
print('x /= b:', x)

x = a
x %= b      #* x = x % 2 = 1
print('x %= b:', x)

x = a
x //= b     #* x = x // 2 = 3
print('x //= b:', x)

x = a
x **= b     #* x = x ** 2 = 49
print('x **= b:', x)


print('0**0 = ', 0**0) # *0**0 = 1
print('2**-3 = ', 2**-3) # *2**-3 = 0.125
print('(1/3)**-2 = ', (1/3)**-2) # *(1/3)**-2 =  9.000000000000002



print("a" in {"a", "b", "c"} ) #True
print("a" in 'carina' )        #True
print("a" in 'beso' )          #False