class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b


class TesteCalculadora:
    def __init__(self) -> None:
        self.calculadora = Calculadora()
        
    def test_soma(self):
        assert self.calculadora.soma(1, 1) == 2
        assert self.calculadora.soma(-1, 1) == 0 
        assert self.calculadora.soma(0, 0) == 0

    def test_sub(self):
        assert self.calculadora.sub(5, 3) == 2
        assert self.calculadora.sub(-1, -1) == 0
        assert self.calculadora.sub(5, 10) == -5