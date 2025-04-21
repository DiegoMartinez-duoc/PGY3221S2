document.getElementById("ir-registro").addEventListener("click", function(event) {
    window.location.href = "registro.html";
})


document.getElementById("registro-formulario").addEventListener("submit", function(event) {
    event.preventDefault();
    let email = document.getElementById("email-input").value;
    let password = document.getElementById("contrasena-input").value;
    
    let usuario = JSON.parse(sessionStorage.getItem("usuario"));

    if (password === "admin" && email === "admin") {
        alert("Inicio de sesion exitoso");
        sessionStorage.setItem("sesionIniciada", "true");
        sessionStorage.setItem("admin", "true");
        window.location.href = "index.html";
    }

    
    if (usuario.contrasena == password && (usuario.correo == email || usuario.usuario == email)) {
        alert("Inicio de sesion exitoso");
        sessionStorage.setItem("sesionIniciada", "true");
        window.location.href = "index.html";
    } else {
        alert("No existe usuario con este nombre/correo o bien la contraseña es incorrecta");
    }
});

document.querySelector(".titulo").addEventListener("click", function() {
    window.location.href = "index.html";
});