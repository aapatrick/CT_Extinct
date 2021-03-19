//Some JavaScript to enable show/hide functionality
$("#eyeIcon").click(function () {
    var inputPw = document.getElementById("InputPassword1");
    var eyeIcon = document.getElementById("eyeIcon");
    if (inputPw.type == "password") {
        inputPw.type = "text";
        eyeIcon.className = "fas fa-eye";
    } else {
        inputPw.type = "password";
        eyeIcon.className = "fas fa-eye-slash";
    }
});

//Some Jquery to create nav bar "active" functionality
var url = window.location.href; // getting the current url
$("li .nav-link").removeClass("active"); // removing any classes with the word active
if (url === "http://kunet.kingston.ac.uk/k1739510/BerWynBusesA1/controller/index_controller.php") {
    $("#nav-home").addClass("active"); //adding the word active to class related to index.php
} else if (url === "http://kunet.kingston.ac.uk/k1739510/BerWynBusesA1/controller/aboutUs_controller.php") {
    $("#nav-aboutUs").addClass("active");
} else if (url === "http://kunet.kingston.ac.uk/k1739510/BerWynBusesA1/controller/fleet_controller.php") {
    $("#nav-fleet").addClass("active");
} else if (url === "http://kunet.kingston.ac.uk/k1739510/BerWynBusesA1/controller/contactUs_controller.php") {
    $("#nav-contactUs").addClass("active");
}

//AJAX Implementation
//creating an event Listener
console.log("outside")
function loadText(event){
    event.preventDefault()
   
    
    
    //creating an XHR Object
    var xhr = new XMLHttpRequest();
    // OPEN - Type, url/file, async
    console.log(xhr);
    xhr.open('POST','../view/sample.txt', true);

    xhr.onload = function(){
        if(this.status ==200)
        {
             console.log(this.responseText);
             document.getElementById('text').innerHTML = this.responseText; 
        }
        else if(this.status =404)
        {
            document.getElementById('text').innerHTML = 'Not Found'; 
        }
    }
    xhr.onerror = function(){
        console.log('Request Error....');
    }
    //sending request
    xhr.send();
}

$('#ajaxSearch').click(function(e){
    console.log("fuck this", e)
    loadText(e)
});

