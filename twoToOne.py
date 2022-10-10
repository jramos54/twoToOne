'''
La funcion acepta dos string a y b, y con  ellas
las combina para obtener la maxima cadena posible
sin  repeticion y ordenada
'''
def longest(a1, a2):
# se concatena a1+a2
# se convierte a set y despues a list.
# se concatena el list resultante en una nueva string
    newString=''.join(list(set(a1+a2)))
# se ordena el nuevo string
    sortString=sorted(newString)
# se convierte el resultado del ordenamiento a string y se entrega el resultado
    return ''.join(sortString)