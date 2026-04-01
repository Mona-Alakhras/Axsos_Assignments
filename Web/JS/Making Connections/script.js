 var h2 = document.querySelector("#name");
function edit(){
  h2.innerText = "Todd E";
}

function removeUser(id){
  var element =document.querySelectorAll(".user-connection");
  for(var i = 0; i < element.length; i++){
    if(element[i].id == id){
      element[i].remove();
    }
  }
  document.querySelector(".circle-nav").innerHTML--;
}

