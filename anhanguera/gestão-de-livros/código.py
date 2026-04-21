import matplotlib.pyplot as plt
# Passo 1: Estrutura do Livro
class Livro:
 def __init__(self, titulo, autor, genero, quantidade):
 self.titulo = titulo
 self.autor = autor
 self.genero = genero
 self.quantidade = quantidade
# Passo 2: Lista de Armazenamento
biblioteca = []
# Passo 3: Funções de Gerenciamento
def cadastrar_livro(t, a, g, q):
 biblioteca.append(Livro(t, a, g, q))
 print(f"Livro '{t}' cadastrado!")
def listar_todos():
 print("\n--- Lista de Livros ---")
 for b in biblioteca:
 print(f"{b.titulo} ({b.genero}) - Qtd:
{b.quantidade}")
def buscar_livro(nome):
 for b in biblioteca:
 if b.titulo.lower() == nome.lower():
 print(f"Encontrado: {b.titulo} de {b.autor}")
 return
 print("Não encontrado.")
# Passo 4: Gráfico Simples
def gerar_grafico():
 generos = [b.genero for b in biblioteca]
 # Conta quantos de cada gênero existem
 counts = {g: generos.count(g) for g in set(generos)}

 plt.bar(counts.keys(), counts.values())
 plt.title("Livros por Gênero")
 plt.show()
# Passo 5: Teste Rápido
cadastrar_livro("Brawl Stars", "Supercell", "Ação", 10)
cadastrar_livro("O Hobbit", "Tolkien", "Fantasia", 5)
cadastrar_livro("1984", "Orwell", "Distopia", 8)
cadastrar_livro("A Hora da Estrela", "Clarice", "Romance",
3)
listar_todos()
buscar_livro("O Hobbit")
gerar_grafico()
