#TDD str: Son un o cadena de caracteres, entrecomillados por comillas dobles o simples (apostrofe).
# Con el operador “+” puedes “Concatenar” varios str para formar uno.
# “\” es el carácter de escape. \n, \t son sentencias de escape para str 

#?ASIGNACION
nombre = 'Edily'
apellido = "Mora"
apellido_dos = "Di' martino"

#?CONTATENACION
print(nombre+" "+apellido_dos)

#?TEXTUALIZACION: MOSTRAR COMILLAS
print(""" ni nombre es Edily Di'martino' """)#!SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("""ella dijo "que no" """) 
print(''' ella dijo "que no" ''') 

#?SALTO DE LINEA
print(
"""Linea 1 
Linea 2
Linea 3""")
print('Linea 4 \nLinea 5 \nLinea 6 \n')

#?TABULACION
print('Nombre \tEddad \tPeso\t \n Maria \t22 \t60.66')

#?ESCAPE
#print('C:\Users\edily\Desktop\Modulo-1-Py') #!SyntaxError: (unicode error) 'unicodeescape'...
print('C:\\Users\\edily\\Desktop\\Modulo-1-Py') #
print("ella dijo \"que no\" ") 


#& ⛹🏽⛹🏽⛹🏽⛹🏽 EJERCICIO 2: Haz un print() saludando señalando tu nombre entrecomillas, di: "Mi nombre es: "Maria Perez" "