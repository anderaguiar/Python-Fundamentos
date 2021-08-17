import modulos
import cherrypy


class CadUsuario:
    _cp_config = {'tools.sessions.on': True}

    @cherrypy.expose
    def index(self):
        user = cherrypy.session.get('user')
        if user == None:
            raise cherrypy.HTTPRedirect('/.')  # volta para pagina de login
        else:
            yield modulos.header
            yield modulos.menutopo(user)
            yield '''<div class="container-fluid" style="margin-top:110px; text-align:left">'''
            arq = open('templates/cadusuario.html', 'r')
            yield arq.read()
            yield '</div>'
            yield modulos.base