const sesion = sessionStorage.getItem("sesionIniciada");





document.querySelectorAll(".boton-like").forEach((boton) => {
    boton.addEventListener("click", function () {
        // if (sesion !== "true") {
        //     window.location.href = "inicio.html";
        //     return;
        // }

        
        const cantidadElemento = this.nextElementSibling.querySelector("#cantidad");

        if (cantidadElemento) {
            
            let cantidad = parseInt(cantidadElemento.textContent.replace(/\D/g, ""), 10);
            cantidad++;
            cantidadElemento.textContent = cantidad; 
        }
    });
});

// document.querySelectorAll(".boton-foro").forEach((boton) => {
//     boton.addEventListener("click", function () {
//         // if (sesion !== "true") {
//         //     window.location.href = "inicio.html";
//         //     return;
//         // }

//         const urlDestino = this.getAttribute("data-url");
//         if (urlDestino) {
//             window.location.href = urlDestino;
//         }

//     });
// });



const track = document.getElementById("juegos");

let seleccion = "crearHilo";


window.onmousedown = e => {
    track.dataset.mouseDownAt = e.clientX;
    isDragging = false;
}

window.onmouseup = () => {
    track.dataset.mouseDownAt = "0";
    if (isDragging) {
        track.dataset.prevPercentage = track.dataset.percentage;
    }
}

window.onmousemove = e => {

    if (parseFloat(track.dataset.mouseDownAt) === 0) return;

    isDragging = true;

    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
        maxDelta = window.innerWidth / 2;

    const percentage = (mouseDelta / maxDelta) * -100,
        nextPercentage = parseFloat(track.dataset.prevPercentage) + percentage;

    track.dataset.percentage = Math.max(Math.min(nextPercentage, -16), -84);

    track.animate({
        transform: `translate(${Math.max(Math.min(nextPercentage, -16), -84)}%, -50%)`
    }, { duration: 1200, fill:"forwards" });
    
    for (const imgen of track.getElementsByClassName("imagen")) {
        imgen.animate({
            objectPosition: `${100 + Math.max(Math.min(nextPercentage, -16), -84)}% center`
        }, { duration: 1200, fill: "forwards" });
    }

    console.log("nextPercentage:", track.dataset.percentage); // Debug

    if (track.dataset.percentage >= -65 && track.dataset.percentage < -45) {
        seleccion = "crearHilo";
       
    }  else if (track.dataset.percentage < -75) {
        seleccion = "miCuenta";
        
    } else if (track.dataset.percentage > -35) {
        seleccion = "hilosCreados";
        
    }

    document.getElementById("input-url").textContent = seleccion;
    document.getElementById("input-url").value = seleccion;
    console.log(seleccion);
}

document.getElementById("form-envio").addEventListener("submit", function(event) {
    document.getElementById("input-url").value = seleccion;
    console.log("Enviado:", seleccion); // Debug
});

