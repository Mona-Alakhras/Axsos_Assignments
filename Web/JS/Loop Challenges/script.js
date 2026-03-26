/*display odd numbers 1-20*/
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}

/*decreasing multiples of 3 from 100 to 0*/
for (let i = 100; i >= 0; i--) {
    if (i % 3 === 0) {
        console.log(i);
    }
}

/*displaying the sequence 4, 2.5, 1, -0.5, -2, -3.5*/
let num = 4;
for (let i = 0; i < 6; i++) {
    console.log(num);
    num -= 1.5;
}

/*display the sum from 1 to 100*/
let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum += i;
}
console.log(sum);

/*display the factorial of 12*/
let factorial = 1;
for (let i = 1; i <= 12; i++) {
    factorial *= i;
}
console.log(factorial);