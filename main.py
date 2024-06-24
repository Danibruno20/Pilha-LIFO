from pilha import Pilha
from livro import Livro

livro1 = Livro("Harry Potter","J. K. Howling", 300)
livro2 = Livro("A probabilidade estatísca do amor a primeira vista","Jannifer E. Smith", 223)
livro3 = Livro("Os Três Mosqueteiros","Alexandre Dumas", 688)

pilha = Pilha()
pilha.add(livro1)
pilha.add(livro2)
pilha.add(livro3)
pilha.imprimir(pilha)