### Parametro posicional
def tipicaFuncion(unpar:int, dospar:int)->None:
#def tipicaFuncion(unpar:int, dospar:int, /)->None
    pass

tipicaFuncion(3, 6)
#unpar = 3
#dospar = 6


### Parametro con valor por defecto
def tipicaFuncion(unpar:int, dospar = 6:int)->None:
    pass

tipicaFuncion(3)
#unpar = 3
#dospar = 6


### Parametro arbitrario
def tipicaFuncion(unpar:int, *dospar:int, content:int)->None:
    pass

tipicaFuncion(3, 6, 6, 6, content=3)


### Parametro nominal
def tipicaFuncion(*,unpar:int, dospar:int)->None
    pass

tipicaFuncion(dospar = 6, unpar = 3)
#unpar = 3
#dospar = 6

### Ejercicio 3
def mtDiv(id:str, *clas:str, content:str)->str
    resultado = ''

    resultado += '<div id="' + id + '" '

    if len(clas) != 0:
        resultado += 'class = "'

        for e in class:
            resultado += e + ','

        resultado += '"'

    return resultado
 

### Ejercicio 5

def myScript(*src:str)->str:
Funcion que tiene como entrada un numero indeterminado de cadenas de caracteres y como salida una cadena de caracteres. Probablemente transforma las entradas en la salida. 