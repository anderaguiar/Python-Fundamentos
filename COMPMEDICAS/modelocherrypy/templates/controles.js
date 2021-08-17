
function EnviaDadosFoto()
{
   event.preventDefault(); // evita refresh da tela
   var tag = document.getElementById("subfoto");
   console.log(tag)
   const URL_TO_FETCH = '/services/recebeFoto';

   var formData = new FormData(document.getElementById("fupload"));

   fetch(URL_TO_FETCH, {
        method: 'post',
        body: formData
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        // result recebe a resposta do módulo dinâmico
        tag.innerHTML = text;
    }).catch(function (error) {
        console.error(error);
    });
}

function EnviaDadosUsuario()
{
   event.preventDefault(); // evita refresh da tela
   var tag = document.getElementById("subFoto");
   console.log(tag)
   const URL_TO_FETCH = '/services/recebeUsuario';

   var formData = new FormData(document.getElementById("fupload"));

   fetch(URL_TO_FETCH, {
        method: 'post',
        body: formData
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        // result recebe a resposta do módulo dinâmico
        tag.innerHTML = text;
    }).catch(function (error) {
        console.error(error);
    });
}

function EnviaDadosConsultaMedica()
{
   event.preventDefault(); // evita refresh da tela
   var tag = document.getElementById("subFoto");
   console.log(tag)
   const URL_TO_FETCH = '/services/recebeConsultaMedica';

   var formData = new FormData(document.getElementById("fupload"));

   fetch(URL_TO_FETCH, {
        method: 'post',
        body: formData
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        // result recebe a resposta do módulo dinâmico
        tag.innerHTML = text;
    }).catch(function (error) {
        console.error(error);
    });
}
