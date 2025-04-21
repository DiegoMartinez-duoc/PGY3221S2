document.getElementById("activar").addEventListener("click", function(event) {
    
    document.getElementById("editar-datos").style.display = "none";
    document.getElementById("editar-formulario").style.display = "block";

    
});

document.getElementById('editar-formulario').addEventListener('submit', function(e) {
    let isValid = true;
    const clearErrors = () => {
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
    };
    clearErrors();

   
    const email = document.getElementById('email-input');
    if (!email.checkValidity()) {
        document.getElementById('email-error').textContent = 'Correo electrónico inválido';
        isValid = false;
    }


    if (!isValid) {
        e.preventDefault();
    }
});