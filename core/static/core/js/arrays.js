$("#btn-submit").on("click", function(){
    $.getScript("core/static/core/js/script_key.js", function() {
        validacionFormulario();
    })

    const users = [];
    if (validacionFormulario()){
        let nombre_user = $("#txtNombre").val();
        let apellido_user = $("#txtApellido").val();
        let rut_user = $("#txtRut").val();
        let fecha_user = $("#txtFecha").val();
        let direccion_user = $("#txtDireccion").val();
        let comuna_user = $("#cmbComuna").val();
        let correo_user = $("#txtCorreo").val();
        let password_user = $("#txtContrasena").val();
        let asunto_user = $("#asunto").val();
        let comentario_user = $("#valComentario").val();

        

        const user = {
            nombre: nombre_user,
            apellido: apellido_user,
            rut: rut_user,
            fecha: fecha_user,
            direccion: direccion_user,
            comuna: comuna_user,
            correo: correo_user,
            password: password_user,
            asunto: asunto_user,
            comentario: comentario_user
        }

        users.push(user);
        Swal.fire({
            icon: 'success',
            title: 'Registrado satisfactoriamente',
            html:
            '<label for="swal-input1">Nombre</label>' + 
            `<input id="swal-input1" class="swal2-input" value="${user.nombre}" readonly>` +
            '<label for="swal-input2">Apellido</label>' +
            `<input id="swal-input2" class="swal2-input" value="${user.apellido}" readonly>` 
        })
        Swal.disableInput();
        
        
    }
    
})

