class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Email:", self.email)


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina

    def exibir_perfil(self):
        super().exibir_perfil()
        print("Disciplina:", self.disciplina)


class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula

    def exibir_perfil(self):
        super().exibir_perfil()
        print("Matrícula:", self.matricula)


professor1 = Professor(
    "Carlos Silva",
    "123.456.789-00",
    "carlos@email.com",
    "Matemática"
)

aluno1 = Aluno(
    "Ana Souza",
    "987.654.321-00",
    "ana@email.com",
    "2026001"
)


print("=== PERFIL DO PROFESSOR ===")
professor1.exibir_perfil()

print("\n=== PERFIL DO ALUNO ===")
aluno1.exibir_perfil()