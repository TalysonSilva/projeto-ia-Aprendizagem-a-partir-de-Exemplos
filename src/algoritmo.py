from .modelo import Hipotese
from .modelo import Hipotese

class EspacoVersao:
    def __init__(self, num_atributos, dominios):
        self.num_atributos = num_atributos
        self.dominios = dominios

        # G começa com a hipótese mais geral:
        self.G = [Hipotese(['?'] * num_atributos)]
        # S começa com a hipótese mais específica:
        self.S = [Hipotese([None] * num_atributos)]

    def treinar(self, exemplo):
    #Ajusta o espaço de versão com base em um novo exemplo
        if exemplo.e_positivo:
            # Prunagem: Remove de G o que for inconsistente com o positivo 
            self.G = [g for g in self.G if g.cobre(exemplo.atributos)]
            # Generalização: Ajusta S para cobrir o exemplo positivo 
            novos_s = []
            for s in self.S:
                if not s.cobre(exemplo.atributos):
                    hipotese_generica = self._generalizar_minimo(s, exemplo.atributos)
                    # Mantém apenas se for consistente com G
                    if any(g.cobre(hipotese_generica.atributos) for g in self.G):
                        novos_s.append(hipotese_generica)
                else:
                    novos_s.append(s)
            self.S = self._remover_redundantes(novos_s, "S")
            
        else:  
            self.S = [s for s in self.S if not s.cobre(exemplo.atributos)]
            # Especialização: Ajusta G para excluir o exemplo negativo 
            novos_g = []
            for g in self.G:
                if g.cobre(exemplo.atributos):
                    especializacoes = self._especializar_minimo(g, exemplo.atributos)
                    # Mantém apenas se for consistente com S
                    for espec in especializacoes:
                        if any(espec.cobre(s.atributos) for s in self.S):
                            novos_g.append(espec)
                else:
                    novos_g.append(g)
            self.G = self._remover_redundantes(novos_g, "G")

    def _generalizar_minimo(self, s, atrs):
        #Torna a hipótese S mais geral para incluir o exemplo.
        novo_atrs = list(s.atributos)
        for i in range(self.num_atributos):
            if novo_atrs[i] is None:
                novo_atrs[i] = atrs[i]
            elif novo_atrs[i] != atrs[i]:
                novo_atrs[i] = '?'
        return Hipotese(novo_atrs)

    def _especializar_minimo(self, g, atrs):
        #Cria versões mais específicas de G que excluem o exemplo negativo.
        especializacoes = []
        for i in range(self.num_atributos):
            if g.atributos[i] == '?':
                for valor in self.dominios[i]:
                    if valor != atrs[i]:
                        nova_lista = list(g.atributos)
                        nova_lista[i] = valor
                        especializacoes.append(Hipotese(nova_lista))
        return especializacoes

    def _remover_redundantes(self, lista, tipo):
        #Limpa o conjunto para manter apenas as hipóteses limites
        resultado = []
        for h in lista:
            if tipo == "S":
                # Em S, removemos as que são mais gerais que outras em S
                if not any(h.cobre(outra.atributos) and h != outra for outra in lista):
                    resultado.append(h)
            else: 
                # Em G, removemos as que são mais específicas que outras em G
                if not any(outra.cobre(h.atributos) and h != outra for outra in lista):
                    resultado.append(h)
        return list(set(resultado))