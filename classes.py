import requests

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
        return f"Correção enviada para {self.aluno.nome}" if self.aluno else "Correção enviada"


import requests
import json

class APIAnalise:
    def __init__(self, url="http://localhost:11434/api/generate"):
        self.url = url

    def analisar_codigo(self, codigo):
        payload = {
            "model": "llama3.2",
            "prompt": f"Corriga e melhore este código: {codigo}",
            "stream" : False
        }

        try:
            response = requests.post(self.url, json=payload, stream=True)

            if response.status_code == 200:
                resultado_final = resultado_final = response.json()['response']

                return Correcao(1, resultado_final, None)
            else:
                return Correcao(1, "Falha ao analisar código", None)

        except requests.RequestException as e:
            return Correcao(1, f"Erro ao conectar com a API: {e}", None)

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
    api_analise = APIAnalise()

    aluno1 = Aluno(1, "123", "João", "j")
    sistema.cadastrar_usuario(aluno1)

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = sistema.autenticar_login(email, senha)

    if usuario:
        print(f"Bem-vindo, {usuario.nome}!")

        if isinstance(usuario, Aluno):
            script_codigo = input("Digite seu código para análise: ")
            correcao = api_analise.analisar_codigo(script_codigo)
            print("\nCódigo corrigido pela IA:")
            print(correcao.codigo_corrigido)
    else:
        print("Login falhou. Verifique suas credenciais.")


if __name__ == "__main__":
    main()
