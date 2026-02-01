class Exemplo:
    def __init__(self, atributos, rotulo):
        self.atributos = atributos
        self.e_positivo = (rotulo.lower() == "positivo")

class Hipotese:
    def __init__(self, atributos):
        self.atributos = atributos

    def cobre(self, exemplo_atributos):
       #Verifica se a hipótese é consistente com o exemplo
        for h, e in zip(self.atributos, exemplo_atributos):
            if h != '?' and h != e:
                return False
        return True