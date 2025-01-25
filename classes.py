class Usuario:
    def __init__(self, id, senha, nome, email):
        self.id = id
        self._senha = senha  # Atributo privado
        self.nome = nome
        self.email = email

    def autenticar(self, senha):
        return self._senha == senha


class Aluno(Usuario):
    def __init__(self, id, senha, nome, email):
        super().__init__(id, senha, nome, email)
        self.scripts_enviados = []

    def enviar_codigo(self, script):
        self.scripts_enviados.append(script)
        return f"Código enviado com sucesso: {script}"


class Professor(Usuario):
    def __init__(self, id, senha, nome, email):
        super().__init__(id, senha, nome, email)
        self.turmas = []
        self.duvidas = []

    def responder_duvida(self, duvida, resposta):
        duvida.resposta = resposta
        return f"Resposta enviada: {resposta}"


class Turma:
    def __init__(self, id, professor):
        self.id = id
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos]


class Duvida:
    def __init__(self, id, aluno, conteudo):
        self.id = id
        self.aluno = aluno
        self.conteudo = conteudo
        self.resposta = None

    def registrar_duvida(self):
        return f"Dúvida registrada: {self.conteudo}"


class Script:
    def __init__(self, id, codigo):
        self.id = id
        self.codigo = codigo
        self.correcao = None

    def vincular_correcao(self, correcao):
        self.correcao = correcao
        return f"Correção vinculada ao script {self.id}"


class Correcao:
    def __init__(self, id, codigo_corrigido, aluno):
        self.id = id
        self.codigo_corrigido = codigo_corrigido
        self.aluno = aluno

    def enviar_aluno(self):
        return f"Correção enviada para {self.aluno.nome}"


class APIAnalise:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def analisar_codigo(self, codigo):
        return Correcao(1, f"Código corrigido: {codigo}", None)  # Simula uma correção


class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def autenticar_login(self, email, senha):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.autenticar(senha):
                return usuario
        return None


def main():
    sistema = Sistema()

    # Criando usuários de exemplo
    aluno1 = Aluno(1, "senha123", "João", "joao@email.com")
    professor1 = Professor(2, "prof456", "Maria", "maria@email.com")
    
    sistema.cadastrar_usuario(aluno1)
    sistema.cadastrar_usuario(professor1)

    # Simulação de login
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = sistema.autenticar_login(email, senha)

    if usuario:
        print(f"Bem-vindo, {usuario.nome}!")

        if isinstance(usuario, Aluno):
            script_codigo = input("Digite seu código para envio: ")
            script = Script(1, script_codigo)
            print(usuario.enviar_codigo(script.codigo))

        elif isinstance(usuario, Professor):
            print("Você pode responder dúvidas dos alunos.")
    else:
        print("Login falhou. Verifique suas credenciais.")


if __name__ == "__main__":
    main()
