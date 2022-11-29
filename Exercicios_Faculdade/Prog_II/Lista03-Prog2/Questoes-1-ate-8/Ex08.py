class Ponto:
    # Construtor
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def imprime_coord(self):
        print(f"Coordenada X: {self.x}")
        print(f"Coordenada Y: {self.y}")

class Reta:
    def __init__(self, ax: float, ay: float, bx: float, by: float):
        self.a = Ponto(ax, ay)
        self.b = Ponto(bx, by)

    def mostra(self):
        print("Coordenadas da reta...")
        print(f"Coordenadas do ponto A: ")
        self.a.imprime_coord()
        print(f"Coordenadas do ponto B: ")
        self.b.imprime_coord()

class Principal:
    reta = Reta(1, 2, 3, 4)
    reta.mostra()
