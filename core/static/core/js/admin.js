document.getElementById("cerrar-sesion").addEventListener("click", function(event) {
    
    sessionStorage.setItem("sesionIniciada", "false");
    window.location.href = "index.html";
})