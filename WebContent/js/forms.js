function checkName() {

    var error = false;
    var contactName = document.getElementById("contactName").value;
    
    if(contactName == ""){
        var errorName = document.getElementById("errorName");
        errorName.classList.remove("hide");
        document.getElementById("divName").classList.add("has-error");
        document.getElementById("glyphName").classList.remove("hide");
        error = true;
    }

    if(!error){
        return true;
    } else {
        console.log('Wystąpił błąd');
        return false;
    }
}

function checkEmail(){

    var error = false;
    var contactEmail = document.getElementById("contactEmail").value;
    

    if(contactEmail == ""){
        var errorEmailIsNull = document.getElementById("errorEmailIsNull");
        errorEmailIsNull.classList.remove("hide");
        document.getElementById("divEmail").classList.add("has-error");
        document.getElementById("glyphEmail").classList.remove("hide");
        error = true;
    } else {
      var regex = /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9]{2,4}$/;
      if(regex.test(contactEmail)==false){
        var errorEmailIsIncorrect = document.getElementById("errorEmailIsIncorrect");
        errorEmailIsIncorrect.classList.remove("hide");
        document.getElementById("divEmail").classList.add("has-error");
        document.getElementById("glyphEmail").classList.remove("hide");
        error=true;
      }
    }

    if(!error){
        return true;
    } else {
        console.log('Wystąpił błąd');
        return false;
    }
    
}

function checkMessage(){

    var error = false;
    var contactMessage = document.getElementById("contactMessage").value;

    if(contactMessage == ''){
        var errorMessage = document.getElementById("errorMessage");
        errorMessage.classList.remove("hide");
        document.getElementById("divMess").classList.add("has-error");
        document.getElementById("glyphMess").classList.remove("hide");
        error = true;
    }

    if(!error){
        return true;
    } else {
        console.log('Wystąpił błąd');
        return false;
    }
}
