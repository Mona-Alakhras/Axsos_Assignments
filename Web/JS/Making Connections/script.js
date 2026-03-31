 var h2 = document.querySelector("#name");
function edit(element){
    h2.innerText = element.value = "Todd E";
}

function removeUser(id){
  var element =document.querySelector(".user-connection");
  element.remove(id);
}