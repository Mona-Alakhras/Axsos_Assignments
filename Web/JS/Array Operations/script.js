/*1-Accessing Elements*/
let colors = ["red", "blue","green", "yellow" ,"purpule"];
console.log(colors[0]);
console.log(colors[1]);
colors[2] = "orange";
console.log(colors);

/*Traversing an Array*/
/*a*/
let numbers = [10, 20, 30, 40, 50];
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
/*b: print elemnts in reverse order*/
for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}

/*Searching in an Array*/
let num = [5,10,15,20,25];
for (let i = 0; i < num.length; i++) {
    if (num[i] === 25) {
       console.log("Found at position: " + i);
    }else {
        console.log("Not found ");
    }
}

/*Sorting an Array*/
let scores = [50 ,20 , 70 , 10 , 40];
scores.sort((a, b) => a - b);
console.log(scores);
scores.sort((a, b) => b - a);
console.log(scores);

let names = ["Shatha" , "Sara" , "Lina" , "Sami","Dalia"];
names.sort();
console.log(names);

/*Inserting Elements*/
let animals = ["dog", "cat", "rabbit"];
animals.push("elephant");
animals.unshift("lion");
animals.splice(2, 0, "tiger");
console.log(animals);

/*Deleting Elements*/
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift();
fruits.pop();
fruits.splice(0, 1);
console.log(fruits);

/*Combining Arrays*/
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let combinedArray = array1.concat(array2);
console.log(combinedArray);

/*Splitting an Array*/
let items = ["a", "b", "c", "d", "e"];
let firstPart = items.slice(0, 3);
let secondPart = items.slice(3);
console.log(firstPart);
console.log(secondPart);

/*Filtering an Array*/
let numbers2 = [1, 5, 10, 15, 20, 25 , 30];
let filteredArray = numbers2.filter(num => num > 15);
console.log(filteredArray);

/*Advanced Challenge*/
let duplicateArray = [1, 2, 2, 3, 4, 4, 5];
let uniqueArray = [...new Set(duplicateArray)];/*set is a built-in object that stores unique values*/
console.log(uniqueArray);

let input = [1,2,3,4,5];
let n =2;
let rotatedArray = input.slice(-n).concat(input.slice(0, 3));
console.log(rotatedArray);
