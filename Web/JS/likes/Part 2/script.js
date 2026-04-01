function increase(id){
    var element = document.getElementById(id);
    var increaseCount = parseInt(element.innerText);
    increaseCount++ ;
    element.innerText = increaseCount;
}