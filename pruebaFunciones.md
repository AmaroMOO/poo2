### Parametro posicional
def tipicaFuncion(unpar:int, dospar:int)->None:
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

tipicaFuncion()