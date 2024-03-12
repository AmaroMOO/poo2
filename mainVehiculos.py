from automovil import automovil
from bicicleta import Bicicleta
from camion import camion
from moto import Moto


def main():
    automovil = automovil(4, "amarillo")
    camion = automovil(8, "azul")
    moto = automovil(3, "rojo")
    bicicleta = automovil(2, "negra")

    camion.info()
    moto.info()
    automovil.info()
    bicicleta.info()

main()
