document.addEventListener("DOMContentLoaded", function() {
    let sesionIniciada = sessionStorage.getItem("sesionIniciada");
    let usuario = JSON.parse(sessionStorage.getItem("usuario"));

    if (sesionIniciada === "true") {
        document.getElementById("nombre-usuario").textContent = usuario.usuario;
        document.getElementById("perfil-usuario").textContent = usuario.usuario;

        document.getElementById("perfil").style.display = "block";
        document.getElementById("cerrar-sesion").style.display = "block";
    }
   
})

document.getElementById("cerrar-sesion").addEventListener("click", function(event) {
    
    sessionStorage.setItem("sesionIniciada", "false");
    window.location.href = "index.html";
})


document.querySelectorAll(".boton-like").forEach((boton) => {
    boton.addEventListener("click", function () {
        const cantidadElemento = this.nextElementSibling.querySelector(".cantidad");

        if (cantidadElemento) {
            let cantidad = parseInt(cantidadElemento.textContent.replace(/\D/g, ""), 10);
            cantidad++;
            cantidadElemento.textContent = cantidad; 
        }
    });
});

document.querySelector(".titulo").addEventListener("click", function() {
    window.location.href = "index.html";
});