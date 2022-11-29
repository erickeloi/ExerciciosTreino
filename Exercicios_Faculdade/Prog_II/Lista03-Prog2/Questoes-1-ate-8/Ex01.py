class Circuito:
    # Construtor
    def inicializa(self, x: int = 0, y: int = 0, raio: int = 0) -> None:
        self.x: int = x
        self.y: int = y
        self.raio: int = raio

    # Definindo Getters
    def get_raio(self):
        return self._raio
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

    def move_x_coord(self, valor):
        self._x = self._x + valor
    
class Principal:
    # Sinta-se Livre para alterar os valores de Raio e Coordenadas na instanciação da classe circuito abaixo.
    circuito = Circuito()
    circuito.inicializa()

    print(f'Raio do Circulo: {circuito.get_raio()}')
    print(f'Coordenada X: {circuito.get_x()}')
    print(f'Coordenada Y: {circuito.get_y()}')
    print("Deslocando Coordenada X em + 17 unidades...")
    circuito.move_x_coord(17)
    print(f'Coordenada X: {circuito.get_x()}')

main = Principal()
