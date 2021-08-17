import os

import cherrypy

from modelocherrypy.infra.conexaoMongoDB import ConexaoMongoDB
from modelocherrypy.model.dados_medicos import DadosMedicos
from modelocherrypy.model.usuario import Usuario
from modelocherrypy.modulos import resultpesquisa


class Services:
    _cp_config = {'tools.sessions.on': True}

    @cherrypy.expose
    def index(self):
        user = cherrypy.session.get('user')
        if user == None:
            raise cherrypy.HTTPRedirect('/.')  # volta para pagina de login


    @cherrypy.expose
    def recebeFoto(self, autor, date, title, patient, keywords, especiality, diagnostic, foto):

        upload_path = os.path.dirname(__file__)
        upload_path = upload_path + '\\imagens'
        upload_file = os.path.join(upload_path, foto.filename)

        file_extention = os.path.splitext(foto.filename)
        if file_extention[1] == '.jpg' or file_extention[1] == '.png':
            arq=open(upload_file, 'wb')
            while True:
                data = foto.file.read(8192)
                if not data:
                    break
                arq.write(data)
            arq.close()

            # insere no banco de dados
            banco = ConexaoMongoDB('MedicoDB')
            file = foto.filename
            dmedicos = DadosMedicos(autor, file, date, title, patient, keywords, especiality, diagnostic)
            ret = banco.inserir(dmedicos, 'ImgMedicas')
            if ret:
                return f"Dados médicos do {patient}, foi cadastrado com sucesso"
            else:
                return f"Erro ao tentar cadastrar os dados do paciente: {patient}."
        else:
            return f"Selecione Imagens com extensão *.jpg ou *.png"



    @cherrypy.expose
    def recebeUsuario(self, nome, email, senha):
        # define o banco de dados
        banco = ConexaoMongoDB('MedicoDB')
        # verifica se o usuário existe
        ret = []
        # dicionario - query filtro de pesquisa
        usu = {}
        usu['email'] = email
        # buscar na coleção com a query
        ret = banco.buscar('Usuarios', usu)
        if ret.__len__() > 0:
            return f"Este usuário {email}, já existe no banco de dados"
        else:
            usu = Usuario(nome, email, senha)
            ret = banco.inserir(usu, 'Usuarios')
            if ret:
                return f"Usuário {email}, foi cadastrado com sucesso"
            else:
                return f"Erro ao tentar cadastrar o usuário: {email}."


    @cherrypy.expose
    def recebeConsultaMedica(self, filtro, valor):
        ret = []
        # define o banco de dados
        banco = ConexaoMongoDB('MedicoDB')

        # dicionario - query com filtro de pesquisa com regex
        query = {}
        query[filtro] = {"$regex": "^"+valor+""}

        # buscar na coleção com a query
        ret = banco.buscar('ImgMedicas', query)
        if ret.__len__() > 0:
            return resultpesquisa(ret)