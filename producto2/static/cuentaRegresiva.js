   // Establecer la fecha de destino
   var countDownDate = new Date("Jul 11, 2024 18:00:00").getTime();

   // Actualizar la cuenta regresiva cada segundo
   var x = setInterval(function() {
       
       // Obtener la fecha y hora actuales
       var now = new Date().getTime();
       
       // Calcular la diferencia entre la fecha actual y la fecha de destino
       var distance = countDownDate - now;
       
       // Calcular el tiempo para días, horas, minutos y segundos
       var days = Math.floor(distance / (1000 * 60 * 60 * 24));
       var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
       var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
       var seconds = Math.floor((distance % (1000 * 60)) / 1000);
       
       // Mostrar el resultado en el elemento con id="cuentaRegresiva"
    //    document.getElementById("cuentaRegresiva").innerHTML = days + " Días " + hours + " Horas "
    //    + minutes + " Minutos " + seconds + " Segundos ";
    document.getElementById("cuentaRegresiva").innerHTML = `
    <div class="time-box">
        <div class="time-unit">${days}</div>
        <div class="time-label">Días</div>
    </div>
    <div class="time-box">
        <div class="time-unit">${hours}</div>
        <div class="time-label">Horas</div>
    </div>
    <div class="time-box">
        <div class="time-unit">${minutes}</div>
        <div class="time-label">Minutos</div>
    </div>
    <div class="time-box">
        <div class="time-unit">${seconds}</div>
        <div class="time-label">Segundos</div>
    </div>
`;
       // Si la cuenta regresiva termina, mostrar un mensaje
       if (distance < 0) {
           clearInterval(x);
           document.getElementById("cuentaRegresiva").innerHTML = "¡La cuenta regresiva ha terminado!";
       }
   }, 1000);