class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem / 100)


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


livro1 = Livro("O Hobbit", 50.00, "J.R.R. Tolkien")
eletronico1 = Eletronico("Fone de Ouvido", 100.00, "110V")


livro1.aplicar_desconto(15)
eletronico1.aplicar_desconto(10)


print("=== LIVRO ===")
print("Nome:", livro1.nome)
print("Autor:", livro1.autor)
print("Novo preço: R$", livro1.preco)

print("\n=== ELETRÔNICO ===")
print("Nome:", eletronico1.nome)
print("Voltagem:", eletronico1.voltagem)
print("Novo preço: R$", eletronico1.preco)