class Livro:
  def crie_pilha():
    from pilha import Pilha
    return Pilha()

  def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.proximo = None

  def add_livro(self, livro):
    livro.proximo = self.topo
    self.topo = livro

  def remover_livro(self):
    self.topo = self.topo.proximo
  
  def __repr__(self):
    return f"Titulo: {self.titulo}   Autor: {self.autor}     Paginas: {self.paginas}     Proximo da Pilha: {self.proximo}"
