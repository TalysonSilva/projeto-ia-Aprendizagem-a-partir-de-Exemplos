from src.modelo import Exemplo
from src.algoritmo import EspacoVersao

def executar_projeto():
    print(" Sistema de IA: Algoritmo de Eliminação de Candidatos")
    # Definição do Domínio (Requisito: Atributos Relevantes) 
    dominios = [
        ["Vermelho", "Azul", "Verde"],  # Cor
        ["Grande", "Pequeno"],          # Tamanho
        ["Circulo", "Quadrado"]         # Forma
    ]
    
    # Inicialização do Cérebro (Espaço de Versão)
    num_atributos = len(dominios)
    ia = EspacoVersao(num_atributos, dominios)
    
    # Exemplo de Dataset
    """
    dataset = [
        Exemplo(["Vermelho", "Grande", "Circulo"], "positivo"),
        Exemplo(["Azul", "Grande", "Circulo"], "negativo"),
        Exemplo(["Vermelho", "Pequeno", "Circulo"], "positivo"),
        Exemplo(["Vermelho", "Grande", "Quadrado"], "negativo")
    ]
    """
    
    # Conjunto de Exemplos (Dataset) 
    dataset = [
    Exemplo(["Vermelho", "Grande", "Circulo"], "positivo"), 
    Exemplo(["Azul", "Grande", "Circulo"], "negativo"),    
    Exemplo(["Vermelho", "Pequeno", "Circulo"], "positivo"), 
    Exemplo(["Vermelho", "Grande", "Quadrado"], "negativo"), 
    Exemplo(["Verde", "Pequeno", "Circulo"], "negativo"),   
    Exemplo(["Vermelho", "Pequeno", "Circulo"], "positivo"), 
    Exemplo(["Vermelho", "Pequeno", "Triangulo"], "negativo"), 
    Exemplo(["Verde", "Grande", "Circulo"], "negativo"),    
    Exemplo(["Vermelho", "Grande", "Circulo"], "positivo"),  
    Exemplo(["Azul", "Pequeno", "Quadrado"], "negativo")    
]
    print("\nIniciando treinamento...")
    for i, exemplo in enumerate(dataset):
        ia.treinar(exemplo)
        
        print(f"\nApós o exemplo {i+1} {exemplo.atributos} ({'Positivo' if exemplo.e_positivo else 'Negativo'}):")
        print(f"  G (Mais Gerais): {[str(g.atributos) for g in ia.G]}")
        print(f"  S (Mais Específicos): {[str(s.atributos) for s in ia.S]}")

    print("\n" + "="*50)
    print("CONCEITO APRENDIDO (Espaço de Versão Final):")
    print(f"G: {[str(g.atributos) for g in ia.G]}")
    print(f"S: {[str(s.atributos) for s in ia.S]}")
    print("="*50)

if __name__ == "__main__":
    executar_projeto()