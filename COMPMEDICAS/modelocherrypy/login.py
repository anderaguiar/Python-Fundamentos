import cherrypy
import os
from menu import *
from modelocherrypy.cad_imgmedicas import CadImgMedicas
from modelocherrypy.cad_usuario import CadUsuario
from modelocherrypy.con_medicas import ConImgMedicas
from modelocherrypy.services import Services

localDir = os.path.dirname(__file__) 

class Login:
    _cp_config = {'tools.sessions.on': True}
    
    @cherrypy.expose
    def index(self):
        cherrypy.lib.sessions.expire()  # destruindo as sessoes criadas anteriormente
        return '''
%s
<div class="container" style="padding:100px; text-align:center">
<h1 style="text-align:center"> Acesso </h1>
<div class="form-group" id="login">
 <form action="menu" name="login" class="form-horizontal"> 
  <p><input maxlength="200" size="200" name="login" placeholder="informe seu login" class="form-control"></p>
  <p><input maxlength="100" size="100" name="senha" type="password" placeholder="informe sua senha" class="form-control"></p>
  <p><input value="entrar" name="blogin" type="submit" class="btn btn-default"></p>
 </form>
</div></div>
</body></html>'''%(modulos.header)


server_config={'server.socket_host':'127.0.0.1','server.socket_port':8180,}
dir_config={
'/imagens':{'tools.staticdir.on': True, 'tools.staticdir.dir': localDir+'\\imagens'},
'/estilos':{'tools.staticdir.on': True,'tools.staticdir.dir': localDir+'\\estilos'},
'/templates':{'tools.staticdir.on': True, 'tools.staticdir.dir':localDir+'\\templates'},}


cherrypy.config.update(server_config)

root = Login()
root.menu = Menu()
root.imgmedicas = CadImgMedicas()
root.cadusuarios = CadUsuario()
root.conmedicas = ConImgMedicas()
root.services = Services()

# conecta no banco de dados,
# caso não exista é criado o banco e sua estrutura automaticamente
# cria o usuario administrador do sistema
# login= adm@adm.com.br senha= 123

bd = 'MedicoDB'
banco = ConexaoMongoDB(bd)

cherrypy.quickstart(root,config=dir_config)