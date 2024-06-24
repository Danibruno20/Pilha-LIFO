from livro import Livro

class Pilha:
  def __init__(self):
    self.topo = Livro

  def imprimir(self):
    print("-------------------------")
    if self.topo == None:
      print("Lista vazia.")
    else:
      aux = self.topo
      while aux:
        print(aux)
        aux = aux.proximo

  def add(self,livro: Livro):
    if self.topo != None:
      livro.proximo = self.topo
    self.topo = livro
    self.imprimir()

  def remover(self):
    if self.topo != None:
      self.topo = self.topo.proximo
    self.imprimir()