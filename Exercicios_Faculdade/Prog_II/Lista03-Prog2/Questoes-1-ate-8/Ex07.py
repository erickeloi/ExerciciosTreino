class Ponto:
    # Construtor
    def __init__(self):
        self.x: float = 0
        self.y: float = 0
    
    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def imprime_coord(self):
        print(f"Coordenada X: {self.x}")
        print(f"Coordenada Y: {self.y}")

class Principal:
    ponto = Ponto()
    ponto.move(2, 3)
    ponto.imprime_coord()
