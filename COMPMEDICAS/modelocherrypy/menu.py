import modulos
import cherrypy

from modelocherrypy.infra.conexaoMongoDB import ConexaoMongoDB


class Menu:
    _cp_config = {'tools.sessions.on': True}
    def index(self,login='',senha='',blogin=''):
        user=cherrypy.session.get('user')
        if login=='' and user==None:
            raise cherrypy.HTTPRedirect('/.') #volta para pagina de login
        elif user == None and login != '':
            ret = []
            usu = {}
            usu['email'] = login
            usu['senha'] = senha

            # buscar na coleção com a query
            banco = ConexaoMongoDB('MedicoDB')
            ret = banco.buscar('Usuarios', usu)
            if ret.__len__() > 0:
                cherrypy.session['user'] = login
                user=login
                yield modulos.header
                yield modulos.menutopo(user)
                yield '''<div class="container-fluid" style="margin-top:110px; text-align:center">'''
                yield '''
                    <br>
                    <h3>Seja Bem-vindo</h3>
                    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                '''
                yield modulos.base
            else:
                raise cherrypy.HTTPRedirect('/.')  # volta para pagina de login
    index.exposed = True

