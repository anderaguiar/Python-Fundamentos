
header = '''
<html lang="pt-br">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  
  <script src="/templates/controles.js"></script>
  
</head>
<body>'''

base = '''
  <div class="bg-dark text-white"> Desenvolvido por: Anderson Roberto de Aguiar | RA: 9422110289 </div>
  <!-- Modal -->
  <div class="modal fade" id="myModal">
    <div class="modal-dialog">
      <div class="modal-content">

        <!-- Modal Header -->
        <div class="modal-header">
          <h4 class="modal-title">Compartilhar Imagens Médicas</h4>
          <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>

        <!-- Modal body -->
        <div class="modal-body">
          <p>Sistema Web Para Compartilhar Imagens Médicas</p>
          <p>Dev: Anderson Roberto de Aguiar</p>
          <p>RA: 9422110289</p>
        </div>

        <!-- Modal footer -->
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-dismiss="modal">Fechar</button>
        </div>

      </div>
    </div>
  </div>
</html>
'''

def menutopo (user=''):
    return '''
<!-- menu -->
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
      <!-- logo -->
      <a class="navbar-brand" href="http://cherrypy.org"> <img src="/imagens/logo.png"/></a>
      <span class="navbar-text  ml-auto float-right"> usuário: %s </span>

      <!-- Links -->
      <ul class="navbar-nav ml-auto float-right">
        <li class="nav-item">
          <a class="nav-link" href="/imgmedicas">Imagens médicas</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/cadusuarios">Novo usuário</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/conmedicas">Consultar Imagens Médicas</a>
        </li>

        <!-- Dropdown -->
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
            Outras Opções
          </a>
          <div class="dropdown-menu">
            <a class="dropdown-item" data-toggle="modal" data-target="#myModal" href="#">Sobre</a>
            <a class="dropdown-item" href="/.">Logout</a>
          </div>
        </li>
      </ul>
    </nav>    
'''%user

def resultpesquisa(ret):

    html = '''
    <style>
    table {
    border-collapse: collapse;
    border-spacing: 0;
    border: 1px solid #ddd;
    }
    th, td {
    text-aling: left;
    padding: 16px;
    }
    tr:nth-child(even) {
    background-color: #f2f2f2;
    }
    </style>'''
    html += '* clicar na imagem para efetuar o download'
    html += '<div><table id="tabela">'
    html += '<tr><th>Foto</th><th>Autor</th><th>Data</th><th>Titulo</th><th>Paciente</th><th>Palavras chaves</th><th>Especialidade</th><th>Diagnostico</th></tr>'

    for linha in ret:
        html += '<tr><td> <a href="/imagens/%s" download> <img width="50" src="/imagens/%s"/> </a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (linha['filename'],linha['filename'],linha['autor'],linha['date'],linha['title'],linha['patient'],linha['keywords'],linha['especiality'],linha['diagnostic'])

    html += '</table></div></form>'
    return html

