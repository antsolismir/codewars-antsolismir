'''
KATA 7KYU: https://www.codewars.com/kata/5467e4d82edf8bbf40000155/python
'''

def descending_order(num):
    '''
    Ordena los numeros dados de mayor a menor, por ejemplo, si me dan 42145 la solución sería: 54421
    
    --FORMA SIN COMPRIMIR-- 
    numeros = [int(x) for x in str(num)]
    numeros.sort(reverse=True)
    return int(''.join(map(str, numeros)))
    -----------------------
    
    --FORMA COMPRIMIDA-- 
    
    return int(''.join(map(str, sorted([int(x) for x in str(num)], reverse=True))))
    
    **EXPLICACION**
    La funcion sorted devuelve una lista del iterable que se le pasa, como un numero no es un iterable hay que convertirlo en un String, que si lo es.
    Lo aprendido en esta kata es que un str es un iterable, por lo tanto no hace falta pasarlo a una lista, pues ya se puede iterar con el, por lo tanto
    ya se puede utilizar el metodo sorted. Este metodo nos devuelve una lista que, gracias a que esta es un iterable, utilizaremos en la funcion map(function, iterable).
    **NOTA**
    El argumento function, en este caso str, funciona como str(x). Al igual que si me creo una funcion que sea:
        def al_cuadrado(arg):
            return arg*arg
    Los argumento que le paso a map serian: map(al_cuadrado, iterable_ejemplo)
    
    A la funcion join() solo se le puede pasar un iterable que contenga str, si no devuelve TypeError. Esta nos devuel 
    **FIN NOTA**
    La funcion map nos devuelve un iterable. Posteriormente utilizamos join, para añadir a el str '' los elementos de ese iterable.
    **FIN EXPLICACION**
    -----------------------
    
    --MEJOR FORMA--
    
    return int(''.join(sorted(str(num), reverse=True)))
    
    **EXPLICACION**
    Es mejor que la solucion anterior devido al ser un str un iterable, no hace falta pasar el numero a una lista, ni usar map debido a que al no haber una lista con ints no
    hay que pasar cada int a str.
    **FIN EXPLICACION**
    -----------------------
    '''
    return int(''.join(sorted(str(num), reverse=True)))