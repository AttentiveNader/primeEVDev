function validateNB(inputtxt) {
    var phoneno = /^01[0-2,5]{1}[0-9]{8}$/;
    var phoneno2 = /^\+201[0-2,5]{1}[0-9]{8}$/;
    if ( (inputtxt.value.match(phoneno)) || (inputtxt.value.match(phoneno2))){return true;}
    else{
    return false;}
}

document.getElementById("infoForm").addEventListener("submit",(e)=>{
   if(!validateNB(document.getElementById("nb"))){
       e.preventDefault()
       alert("invalid phone number")
   }
});