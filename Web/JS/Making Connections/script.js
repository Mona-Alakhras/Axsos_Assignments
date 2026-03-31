 var h2 = document.querySelector("#name");
function edit(element){
    h2.innerText = element.value = "Todd E";
}

var img = document.querySelectorAll(".user-connection");
function removeUser(element){
    img.remove(element);
}