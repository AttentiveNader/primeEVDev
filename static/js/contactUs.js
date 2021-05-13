
function validateEmail(mail) 
{
 if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(mail))
  {
    return (true)
  }
    // alert("You have entered an invalid email address!")
    return (false)
}
const phoneInputField = document.querySelector("#userPhone");
const phoneInput = window.intlTelInput(phoneInputField, {
  utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});
function handleSubmit(e){
  // e.preventDefault()
  // console.log(e.target)
  console.log
  let errMsg = ""
  let name = document.getElementById("userName");
  let email = document.getElementById("userEmail");
  let phoneNumber = document.getElementById("userPhone");
  let errDev =document.getElementById("contact-error")
  let userMsg = document.getElementById("userMessage")
  if (name.value.length<= 1){
    name.className = "input error-input"
    errMsg = "plz, enter a valid name"
    errDev.style.display = "block";
    errDev.children[1].innerHTML = errMsg
    return
  }else{
    name.className = "input"
    errDev.style.display = "none";
  }
  if (!validateEmail(email.value)){
    // console.log("")
    email.className = "input error-input"
    errMsg = "plz, enter a valid email"
    errDev.style.display = "block";
    errDev.children[1].innerHTML = errMsg
    return
  }else{
    email.className = "input"
    errDev.style.display = "none";
  }

  if(!phoneInput.isValidNumber()){
    phoneNumber.className = "input error-input"
    errMsg = "plz, enter a valid phone"
    errDev.style.display = "block";
    errDev.children[1].innerHTML = errMsg
    return
  }else{
    phone.className = "input"
    errDev.style.display = "none";   
  }
  if (userMsg.value.length <= 5){
    userMsg.className = "input error-input"
    errMsg = "plz, enter a valid message"
    errDev.style.display = "block";
    errDev.children[1].innerHTML = errMsg
    return
  }else{
    userMsg.className = "input"
    errDev.style.display = "none"; 
  }

}

mapboxgl.accessToken = 'pk.eyJ1IjoibmFkZXJheiIsImEiOiJja29raDExcm8wNWFwMnhybW5nenR5eHNmIn0.QsIKcYkHsfuim8TcdR4tyA';
var map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/mapbox/streets-v11', // style URL
center: [31.3141, 30.0491], // starting position [lng, lat]
zoom: 11 // starting zoom
});
var marker = new mapboxgl.Marker()
.setLngLat([31.3141, 30.0491])
.addTo(map);
  //         function initMap() {
  //   // The location of madinet nasr
  //   // 31.3141 
  //   const madinetNasr = { lat:  30.0491, lng: 31.3141 };
  //   // The map, centered at madinetNasr
  //   const map = new google.maps.Map(document.getElementById("map"), {
  //     zoom: 11,
  //     center: madinetNasr,
  //   });
  //   // The marker, positioned at madinetNasr
  //   const marker = new google.maps.Marker({
  //     position: madinetNasr,
  //     map: map,
  //   });
  // }
        window.fbAsyncInit = function() {
          FB.init({
            xfbml            : true,
            version          : 'v10.0'
          });
        };

        (function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = 'https://connect.facebook.net/en_US/sdk/xfbml.customerchat.js';
          fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));