class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self):
        return self.salario_base * 0.05


class Gerente(Funcionario):
    def calcular_bonus(self):
        return super().calcular_bonus() + 1000


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas

    def calcular_bonus(self):
        return self.total_vendas * 0.10


funcionario = Funcionario("Carlos", 3000)
gerente = Gerente("Ana", 5000)
vendedor = Vendedor("João", 2500, 20000)

print(f"Bônus do funcionário: R$ {funcionario.calcular_bonus():.2f}")
print(f"Bônus do gerente: R$ {gerente.calcular_bonus():.2f}")
print(f"Bônus do vendedor: R$ {vendedor.calcular_bonus():.2f}")