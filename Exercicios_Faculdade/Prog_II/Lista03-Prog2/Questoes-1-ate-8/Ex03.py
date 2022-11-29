class Trava:
    def __init__(self) -> None:
        self.quem: str = ""
        self.travado: bool = False

    def trave(self, quem_travar: str) -> None:
        self.quem = quem_travar
        self.travado = True

    def destrave(self, quem_destravar: str) -> None:
        self.quem = quem_destravar
        self.travado = False
    
    def isTravado(self) -> bool:
        return self.travado
    
    # Extra
    def info(self) -> None:
        print(f"Informações do Jogador: {self.quem}")
        print(f"O Jogador encontra-se: {'Travado' if self.travado else 'Destravado'}\n")
    
player1 = Trava()

player1.trave("Jorge")
player1.info()

player1.destrave("Jorge")
player1.info()
