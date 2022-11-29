class Circuito:
    def inicializa(self, x: int = 0, y: int = 0, raio: int = 0) -> None:
        self.x: int = x
        self.y: int = y
        self.raio: int = raio

    def altera_raio(self, novo_valor: int) -> None:
        self.raio = novo_valor

    def retorna_raio(self) -> int:
        return self.raio

    def move_x_coord(self, value: int) -> None:
        self.x = self.x + value
        
    # Definindo Getters
    def get_raio(self):
        return self.raio
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    # Definindo Setters
    def set_raio(self, novo_valor: int):
        self.raio = novo_valor
    def set_x(self, novo_valor: int):
        self.x = novo_valor
    def set_y(self, novo_valor: int):
        self.y = novo_valor

# Sinta-se Livre para alterar os valores de Raio e Coordenadas na instanciação da classe circuito abaixo.
class Principal:
    circuito = Circuito()
    circuito.inicializa(0,0,10)
    print(f'Raio do Circulo: {circuito.retorna_raio()}')
    print(f'Coordenada X: {circuito.x}')
    print(f'Coordenada Y: {circuito.y}')

    print("Movendo circulo para as coord. (1,1)...")
    circuito.set_y(1)
    circuito.set_x(1)
    print(f'Raio do Circulo: {circuito.retorna_raio()}')
    print(f'Coordenada X: {circuito.x}')
    print(f'Coordenada Y: {circuito.y}')

    print("Alterando a coordenada X para 100...")
    circuito.set_x(100)
    print(f'Raio do Circulo: {circuito.retorna_raio()}')
    print(f'Coordenada X: {circuito.x}')
    print(f'Coordenada Y: {circuito.y}')
    
    print(f'Alterando o raio do círculo para 12...')
    circuito.altera_raio(12)
    print(f'Raio do Circulo: {circuito.retorna_raio()}')
    print(f'Coordenada X: {circuito.x}')
    print(f'Coordenada Y: {circuito.y}')

main = Principal()
