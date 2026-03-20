if(number>0){
    console.log("Positive number");
} else {
    console.log("Negative number");
}

let time = new Date().getHours();
if(time < 12){
    console.log("Good morning");
}else{
    console.log("Good afternoon");
}

if(score >= 90){
    console.log("Grade: A");
}else if(score >= 80 && score < 89){    
    console.log("Grade: B");
}else if(score >= 70 && score < 79){
    console.log("Grade: C");
}else if(score >70){
    console.log("Grade: F");
}


let day = "Friday"; 
day = day.toLowerCase();
if (day === "friday" || day === "saturday") {
    console.log("It's Weekend");
} else {
    console.log("It's a Weekday");
}
