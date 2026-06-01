document.querySelector("form").addEventListener("submit", function(e){

    const usuario = document.querySelector('input[name="usuario"]').value;
    const senha = document.querySelector('input[name="senha"]').value;

    if(usuario.length < 3 || senha.length < 3){

        e.preventDefault();

        alert("Preencha corretamente.");

    }

});