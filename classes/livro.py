class Livro:
  def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.proximo = None

  def add_livro(self, livro):
    livro.proximo = self.topo
    self.topo = livro