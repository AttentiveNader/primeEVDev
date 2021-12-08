function validateNB(inputtxt) {
    var phoneno = /^01[0-2,5]{1}[0-9]{8}$/;
    var phoneno2 = /^+201[0-2,5]{1}[0-9]{8}$/;
    if (!(inputtxt.value.match(phoneno)) && !(inputtxt.value.match(phoneno2))){return true;}
    else{ alert("Invalid Phone number");
    return false;}
}