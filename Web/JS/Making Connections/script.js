 var h2 = document.querySelector("#name");
function edit(element){
    h2.innerText = element.value = "Todd E";
}

function removeUser(id){
  var element =document.querySelectorAll(".user-connection");
  for(var i = 0; i < element.length; i++){
    if(element[i].id == id){
      element[i].remove();
    }
  }
}