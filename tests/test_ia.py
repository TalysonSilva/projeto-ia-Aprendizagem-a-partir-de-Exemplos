import unittest
from src.modelo import Hipotese, Exemplo

class TestIA(unittest.TestCase):
    def test_consistencia_hipotese(self):
        #Verifica se o cálculo da consistência está correto.
        h = Hipotese(['?', 'Azul', '?'])
        ex = Exemplo(['Grande', 'Azul', 'Quadrado'], "positivo")
        self.assertTrue(h.cobre(ex.atributos))

    def test_inconsistencia_hipotese(self):
        h = Hipotese(['?', 'Vermelho', '?'])
        ex = Exemplo(['Grande', 'Azul', 'Quadrado'], "positivo")
        self.assertFalse(h.cobre(ex.atributos))

    def test_exemplo_positivo(self):
        ex = Exemplo(['Vermelho', 'Grande', 'Circulo'], "positivo")
        self.assertTrue(ex.e_positivo)
    
    def test_exemplo_negativo(self):
        ex = Exemplo(['Azul', 'Pequeno', 'Quadrado'], "negativo")
        self.assertFalse(ex.e_positivo)
    
    def test_hipotese_atributos(self):
        h = Hipotese(['Vermelho', 'Grande', 'Circulo'])
        self.assertEqual(h.atributos, ['Vermelho', 'Grande', 'Circulo'])

    def test_generalizacao_s(self):
        from src.algoritmo import EspacoVersao
        ia = EspacoVersao(3, [["A", "B"], ["C", "D"], ["E", "F"]])
        ex = Exemplo(["A", "C", "E"], "positivo")
        ia.treinar(ex)
        # S deve ter deixado de ser [None, None, None]
        self.assertEqual(ia.S[0].atributos, ["A", "C", "E"])

    def test_especializacao_g(self):
        from src.algoritmo import EspacoVersao
        ia = EspacoVersao(3, [["Vermelho", "Azul"], ["Grande"], ["Circulo"]])
        # Simula que S já conhece um padrão
        ia.S = [Hipotese(["Vermelho", "Grande", "Circulo"])]
        ex_negativo = Exemplo(["Azul", "Grande", "Circulo"], "negativo")
        ia.treinar(ex_negativo)

        # G não pode mais ser ['?', '?', '?'] se for G sera inconsistente com S
        self.assertNotIn(['?', '?', '?'], [g.atributos for g in ia.G])