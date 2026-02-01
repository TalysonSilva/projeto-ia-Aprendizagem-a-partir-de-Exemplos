# 🤖 Projeto Final: Inteligência Artificial - Espaço de Versão

![Status](https://img.shields.io/badge/Status-Finalizado-green?style=for-the-badge)
![Linguagem](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Paradigma](https://img.shields.io/badge/Paradigma-POO-blue?style=for-the-badge)

Este repositório contém o projeto final da disciplina de **Inteligência Artificial**, focado no tema **Aprendizagem a partir de Exemplos**

## 🎓 Identificação
* **Discente:** Talyson Rodrigues Silva Nascimento
* **Docente:** Marlos Tacio Silva 
* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia de Sergipe - Campus Itabaiana 
* **Prazo Final:** 02/02/2026 

---

## 📝 Descrição do Problema
O objetivo deste projeto é construir um sistema inteligente capaz de realizar **Aprendizagem Indutiva Pura**. O sistema deve encontrar uma hipótese que se ajuste a um conjunto de exemplos de treinamento (descrições e classificações) e generalize bem para novos dados126.

Utilizamos o algoritmo de **Eliminação de Candidatos**, que refina a busca mantendo o conjunto de todas as hipóteses consistentes com os exemplos observados através do **Espaço de Versão**.

---

## ⚙️ Requisitos Técnicos
Conforme as "regras do jogo" estabelecidas pelo professor
* **Orientação a Objetos:** O sistema foi estruturado em classes para representar as entidades do problema.
* **Implementação Manual:** O núcleo do algoritmo foi codificado sem o uso de bibliotecas "caixa-preta".
* **Testes de Unidade:** Verificamos se os métodos funcionam como esperado através de testes unitários.

### 🏗️ Estrutura de Classes
1. **`Exemplo`**: Armazena os atributos e a classificação (positivo/negativo).
2. **`Hipotese`**: Representa uma regra no espaço de busca.
3. **`EspacoVersao`**: O "Cérebro" que gerencia os conjuntos **G** (Mais Gerais) e **S** (Mais Específicos).

---

## 🚀 Como Instalar e Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

2. **Execução dos testes:**
   ```bash
   python -m unittest discover tests

2. **Execução do sistemas:**
   ```bash
   python main.py

--- 

## 📈 Resultado e Analise 

### Apredizando 
o Projeto demonstrou convergência ao processar os exemplos, "apertando" os conjuntos G e S até encontrar a hipótese correta

### Resultado: 

## Execução do Arquivo main.py
![alt text](/img/main-py.png)

## Execução do Teste
![alt text](/img/test.png)