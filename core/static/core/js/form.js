document.getElementById("ocultar").style.display = "none";
document.getElementById("valNombre").style.display = "none";
document.getElementById("valApellido").style.display = "none";
document.getElementById("valDireccion").style.display = "none";
document.getElementById("valCorreo").style.display = "none";
document.getElementById("valRut").style.display = "none";
document.getElementById("valComuna").style.display = "none";
document.getElementById("valContrasena").style.display = "none";


$(".form-control").on("blur", function(){
  validacionFormulario();
});

$("#btn-password").on("click", function(){
  password();
});

function validacionFormulario(){
  $("small").css('color', 'red');
  let nombre = document.getElementById("txtNombre").value;
  let apellido = document.getElementById("txtApellido").value;
  let direccion = document.getElementById("txtDireccion").value;
  let correo = document.getElementById("txtCorreo").value;
  let rut = document.getElementById("txtRut").value;
  let comuna = document.getElementById("cmbComuna").value;
  let contrasena = document.getElementById("txtContrasena").value;

  let nom = validarNombre (nombre);
  let ap = validarApellido(apellido);
  let dir = validarDir(direccion);
  let em = validarEmail(correo);
  let rt =validarRut(rut);
  let com = validarComuna(comuna);
  let pass = validarPass(contrasena);
  valComentario();

  if (nom & ap & dir & em & rt & com & pass){
    return true;
  } 
  return false;

  
}

function validarNombre (nombre){
  if (nombre.trim().length == 0) {
    document.getElementById("valNombre").style.display = "inline";
    document.getElementById("txtNombre").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valNombre").style.display = "none";
    document.getElementById("txtNombre").classList.remove("is-invalid");
    document.getElementById("txtNombre").classList.add("is-valid");
    return true;
  };
}

function validarApellido(apellido) {
  if (apellido.trim().length == 0) {
    document.getElementById("valApellido").style.display = "inline";
    document.getElementById("txtApellido").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valApellido").style.display = "none";
    document.getElementById("txtApellido").classList.remove("is-invalid");
    document.getElementById("txtApellido").classList.add("is-valid");
    return true;
  }
}
//
function validarDir (direccion){
  if (direccion.trim().length == 0) {
    document.getElementById("valDireccion").style.display = "inline";
    document.getElementById("txtDireccion").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valDireccion").style.display = "none";
    document.getElementById("txtDireccion").classList.remove("is-invalid");
    document.getElementById("txtDireccion").classList.add("is-valid");
    return true;
  }
}

function validarEmail(correo) {
  let rgEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
  if (rgEmail.test(correo) == false) {
    document.getElementById("valCorreo").style.display = "inline";
    document.getElementById("txtCorreo").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valCorreo").style.display = "none";
    document.getElementById("txtCorreo").classList.remove("is-invalid");
    document.getElementById("txtCorreo").classList.add("is-valid");
    return true;
  }
}

function validarRut(rut) {
  var Fn = {
    // Valida el rut con su cadena completa "XXXXXXXX-X"
    validaRut : function (rutCompleto) {
      rutCompleto = rutCompleto.replace("‐","-");
      if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
          return false;
      var tmp 	= rutCompleto.split('-');
      var digv	= tmp[1]; 
      var rut 	= tmp[0];
      if ( digv == 'K' ) digv = 'k' ;
      
      return (Fn.dv(rut) == digv );
    },
    dv : function(T){
      var M=0,S=1;
      for(;T;T=Math.floor(T/10))
          S=(S+T%10*(9-M++%6))%11;
      return S?S-1:'k';
    }
  } 

  if (Fn.validaRut(rut) == false) {
    document.getElementById("valRut").style.display = "inline";
    document.getElementById("txtRut").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valRut").style.display = "none";
    document.getElementById("txtRut").classList.remove("is-invalid");
    document.getElementById("txtRut").classList.add("is-valid");
    return true;
  }
}

function validarComuna(comuna) {
  if (comuna == "null") {
    document.getElementById("valComuna").style.display = "inline";
    document.getElementById("cmbComuna").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valComuna").style.display = "none";
    document.getElementById("cmbComuna").classList.remove("is-invalid");
    document.getElementById("cmbComuna").classList.add("is-valid");
    return true;
  }
}

function validarPass(contrasena) {
  let rgPass = /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{6,10}$/;
  if (rgPass.test(contrasena) == false) {
    document.getElementById("valContrasena").style.display = "inline";
    document.getElementById("txtContrasena").classList.add("is-invalid");
    return false;
  }else{
    document.getElementById("valContrasena").style.display = "none";
    document.getElementById("txtContrasena").classList.remove("is-invalid");
    document.getElementById("txtContrasena").classList.add("is-valid");
    return true;
  }
}



function password(){
  let input = document.getElementById("txtContrasena");

  if (input.type == 'password') {
    input.type = 'text';
    document.getElementById('mostrar').style.display = 'none';
    document.getElementById("ocultar").style.display = 'inline';
  }else{
    input.type = 'password';
    document.getElementById('mostrar').style.display = 'inline';
    document.getElementById("ocultar").style.display = 'none';
  }

}

function valComentario(){
  let max_caracteres = 50;
  $('#valComentario').attr('maxlength', max_caracteres);  

  $('#valComentario').keyup(function(){
    let num_caracteres = $('#valComentario').val().length;
    let charRemain = (max_caracteres - num_caracteres);
      

    if(charRemain <= 0){
        document.getElementById("charNum").innerHTML = '<span style="color: red;">Has excedido el límite de '+max_caracteres+' caracteres</span>';
    }else{
        document.getElementById("charNum").innerHTML = charRemain+' caracteres restantes';   
    }
    
  });
}