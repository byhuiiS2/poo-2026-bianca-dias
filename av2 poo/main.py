class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        if not modelo.strip():
            raise ValueError("O modelo não pode ser vazio.")
        self.__modelo = modelo

    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        if not placa.strip():
            raise ValueError("A placa não pode ser vazia.")
        self.__placa = placa.upper()

    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_valor_diaria(self, valor_diaria):
        if valor_diaria <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor_diaria

    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")

        return self.__valor_diaria * dias


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)
        self.set_portas(portas)

    def get_portas(self):
        return self.__portas

    def set_portas(self, portas):
        if portas <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")
        self.__portas = portas

    def calcular_aluguel(self, dias):
        valor_base = super().calcular_aluguel(dias)
        return valor_base + 50


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.set_cilindradas(cilindradas)

    def get_cilindradas(self):
        return self.__cilindradas

    def set_cilindradas(self, cilindradas):
        if cilindradas <= 0:
            raise ValueError("As cilindradas devem ser maiores que zero.")
        self.__cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        valor_base = super().calcular_aluguel(dias)
        return valor_base * 0.90


veiculos = [
    Carro("Fusca", "BIA-0023", 150.00, 4),
    Carro("Camaro amarelo", "DEF-5678", 120.00, 4),
    Moto("Triumph Bobber", "GHI-9012", 80.00, 160),
    Moto("Triumph Rocket III", "JKL-3456", 100.00, 250)
]


def listar_veiculos():
    if not veiculos:
        print("\nNenhum veículo cadastrado.")
        return

    print("\n========== VEÍCULOS CADASTRADOS ==========")

    for veiculo in veiculos:
        print(f"\nModelo: {veiculo.get_modelo()}")
        print(f"Placa: {veiculo.get_placa()}")
        print(f"Valor da diária: R$ {veiculo.get_valor_diaria():.2f}")

        if isinstance(veiculo, Carro):
            print(f"Tipo: Carro")
            print(f"Portas: {veiculo.get_portas()}")

        elif isinstance(veiculo, Moto):
            print(f"Tipo: Moto")
            print(f"Cilindradas: {veiculo.get_cilindradas()}")

    print("\n===========================================")


def cadastrar_veiculo():
    print("\n========== CADASTRAR VEÍCULO ==========")

    try:
        modelo = input("Digite o modelo: ")
        placa = input("Digite a placa: ")
        valor_diaria = float(input("Digite o valor da diária: "))

        print("\nEscolha o tipo:")
        print("1 - Carro")
        print("2 - Moto")

        tipo = int(input("Digite a opção: "))

        if tipo == 1:
            portas = int(input("Digite a quantidade de portas: "))

            novo_veiculo = Carro(
                modelo,
                placa,
                valor_diaria,
                portas
            )

        elif tipo == 2:
            cilindradas = int(input("Digite as cilindradas: "))

            novo_veiculo = Moto(
                modelo,
                placa,
                valor_diaria,
                cilindradas
            )

        else:
            raise ValueError("Tipo de veículo inválido.")

        veiculos.append(novo_veiculo)

    except ValueError as erro:
        print(f"\nErro: {erro}")

    else:
        print("\nVeículo cadastrado com sucesso!")

    finally:
        print("Operação de cadastro finalizada.")


def calcular_aluguel():
    if not veiculos:
        print("\nNenhum veículo cadastrado.")
        return

    print("\n========== CALCULAR ALUGUEL ==========")

    placa = input("Digite a placa do veículo: ").upper()

    try:
        dias = int(input("Digite a quantidade de dias: "))

        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")

        veiculo_encontrado = False

        for veiculo in veiculos:
            if veiculo.get_placa() == placa:
                veiculo_encontrado = True

                valor = veiculo.calcular_aluguel(dias)

                print("\n========== RESULTADO ==========")
                print(f"Modelo: {veiculo.get_modelo()}")
                print(f"Placa: {veiculo.get_placa()}")

                if isinstance(veiculo, Carro):
                    print("Tipo: Carro")
                    print("Taxa de limpeza: R$ 50,00")

                elif isinstance(veiculo, Moto):
                    print("Tipo: Moto")
                    print("Desconto: 10%")

                print(f"Quantidade de dias: {dias}")
                print(f"Valor total: R$ {valor:.2f}")
                print("================================")

                break

        if not veiculo_encontrado:
            raise LookupError("Veículo não encontrado.")

    except ValueError as erro:
        print(f"\nErro: {erro}")

    except LookupError as erro:
        print(f"\nErro: {erro}")

    else:
        print("\nCálculo realizado com sucesso.")

    finally:
        print("Operação de aluguel finalizada.")


def menu():
    while True:
        print("\n")
        print("========================================")
        print("       SISTEMA DE GESTÃO DE FROTA")
        print("========================================")
        print("1 - Listar veículos")
        print("2 - Cadastrar veículo")
        print("3 - Calcular aluguel")
        print("4 - Sair")
        print("========================================")

        try:
            opcao = int(input("Digite uma opção: "))

        except ValueError:
            print("\nErro: digite apenas números.")

        else:
            if opcao == 1:
                listar_veiculos()

            elif opcao == 2:
                cadastrar_veiculo()

            elif opcao == 3:
                calcular_aluguel()

            elif opcao == 4:
                print("\nSistema encerrado.")
                break

            else:
                print("\nErro: opção inexistente. Escolha uma opção de 1 a 4.")

        finally:
            print("\nVoltando ao menu...")


menu()