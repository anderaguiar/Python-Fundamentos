
# class
class Usuario:
    nomeCompleto = None
    email = None
    senha = None

    # constructor
    def __init__(self, nomeCompleto, email, senha):
        self.nomeCompleto = nomeCompleto
        self.email = email
        self.senha = senha

    # set
    def setNomeCompleto(self, nomeCompleto):
        self.nomeCompleto = nomeCompleto
    def setEmail(self, email):
        self.email = email
    def setSenha(self, senha):
        self.senha = senha

    # get
    def getNomeCompleto(self):
        return self.nomeCompleto
    def getEmail(self):
        return self.email
    def getSenha(self):
        return self.senha