class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muestraPunto(self):
        return print('El punto es: ({}, {})'.format(self.x, self.y))
