from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print(f"O carro {self.modelo} está acelerando com velocidade média.")

class Moto(Veiculo):
    def acelerar(self):
        print(f"A moto {self.modelo} está acelerando rapidamente, graças à sua agilidade.")

class Caminhao(Veiculo):
    def acelerar(self):
        print(f"O caminhão {self.modelo} está acelerando lentamente devido ao peso.")

class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"O carro elétrico {self.modelo} está acelerando suavemente e silenciosamente.")

pista_de_corrida = [
    Carro("Honda Civic"),
    Moto("Yamaha YZF-R3"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]

for veiculo in pista_de_corrida:
    veiculo.acelerar()
