from pymongo import *

# class
from modelocherrypy.model.usuario import Usuario


class ConexaoMongoDB(object):
    _con = None
    _db = None
    _collection = None
    _query = None

    # constructor
    def __init__(self, db):
        self._con = MongoClient('localhost', 27017)
        try:
            listadb = self._con.list_database_names()
            if listadb.__contains__(db):
                self._db = self._con[db]
            else:
                self.criarBanco(db)
                self.criarColecao('Usuarios')
                self.inserirUsuarioAdm()
                self.criarColecao('ImgMedicas')
                self._db = self._con[db]
        except:
            return False

    # abrir conexão
    def abrirConexao(self):
        try:
            self._con = MongoClient('localhost', 27017)
        except:
            return False
        return True

    # função para criar o banco de dados
    def criarBanco(self, banco):
        try:
            self._db = self._con[banco]
        except:
            return False
        return True

    # função para criar a coleção em um banco de dados
    def criarColecao(self, colecao):
        try:
            self._collection = self._db[colecao]
        except:
            return False
        return True

    # função para inserir o usuário administrador
    def inserirUsuarioAdm(self):
        try:
            usu = Usuario('administrador', 'adm@adm.com.br', '123')
            self.inserir(usu, 'Usuarios')
        except:
            return False
        return True

    # função para inserir um documento em uma coleção
    def inserir(self, obj, colecao):
        try:
            self._collection = self._db[colecao]
            self._collection.insert_one(obj.__dict__)
        except:
            return False
        return True

    # função para inserir uma coleção de documentos
    def inserir_many(self, lista, colecao):
        try:
            self._collection = self._db[colecao]
            self._collection.insert_many(lista.__dict__)
        except:
            return False
        return True

    # funcao query
    def query(self, query):
        self._query = query

    # função para buscar todos na coleção
    def buscarTodos(self, colecao):
        result = []
        self._collection = self._db[colecao]
        for v in self._collection.find():
            result.append(v)
        return result

    # funcao para buscar na coleção com query
    def buscar(self, colecao, query):
        result = []
        self._query = query
        self._collection = self._db[colecao]
        for v in self._collection.find(self._query):
            result.append(v)
        return result