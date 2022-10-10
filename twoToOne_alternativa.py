'''
Se correra cada letra del alfabeto y despues se verificara la existencia
en la nueva cadena y si el caracter existe en la nueva cadena, se agrega 
a la salida. 
Esto nos da la nueva cadena ordenada y sin repeticion.
Se importo el modulo string para obtener los caracteres ascii a utilizar. 
'''
import string

def longest(a1, a2):
# Se concatena las cadenas
	newstring=a1+a2
# Se genera los caracteres ascii, ya ordenados
	alpha=string.printable
# Se crea la variable de salida
	result=''
# Se recorre cada uno de los caracteres
	for i in alpha:
# Se compara si el caracter esta en la nueva cadena
		if i in newstring:
# Si el caracter esta, se concatena a la variable de salida
			result+=i
	return result
					