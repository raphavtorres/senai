class ControleRemoto:
    # Construtor
    def __init__(self, valor_cor: str, altura: float, profundidade: float, largura: float):
        self.cor = valor_cor
        self.alt = altura
        self.prof = profundidade
        self.larg = largura

    def passar_canal(self, botao):
        if botao == '+':
            print("Próximo canal")
        elif botao == '-':
            print("Canal anterior")
