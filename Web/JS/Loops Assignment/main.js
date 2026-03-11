/* Print numbers from 1 to 10 */
for(var i = 1; i <= 10; i++){
    console.log(i);
}

/*Print Reversed numbers from 10 to 1 */
for(var i = 10; i >= 1; i--){
    console.log(i);
}

/* Print even numbers from 1 to 20 */
for(var i = 2; i <= 20; i += 2){
    console.log(i);
}

/* Print odd numbers from 1 to 20 */
for(var i = 1; i <= 20; i += 2){
    console.log(i);
}

/* Prin the sum of numbers from 1 to 10 */
var sum = 0;
for(var i = 1 ; i <= 10; i++){
    sum += i;
}
console.log("The sum of numbers from 1 to 10 is: " + sum);

/*Print FizzBuzz from 1 to 30 */
for(var i = 1; i <= 30; i++){
    if(i % 3 === 0 && i % 5 === 0){
        console.log('"FizzBuzz"');
    }
    else if(i % 3 === 0){
        console.log('"Fizz"');
    }
    else if(i % 5 === 0){
        console.log('"Buzz"');
    }
    else{
        console.log(i);
    }
}