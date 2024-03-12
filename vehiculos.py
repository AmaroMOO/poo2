class Vehiculo:
    def __init__(self, ruedas:int, color:str) -> None:
        self.ruedas = ruedas
        self.color = color
        ruedas = 0
        color = ""

    def info(self)->None:
        print(self.ruedas, self.color)
