function removeBlanks(str){
    var newStr = "";
    for(var i = 0; i<=str.length-1; i++){
        if(str[i] !== " "){
            newStr+= str[i];
        }
    }
    return newStr;

}
console.log(removeBlanks("Pl ayTha tF nkyM usi c"));

function getDigits(str){
    var newDigit = "";
    for(var i =0; i<= str.length-1; i++){
        if(str[i]>='0' && str[i]<='9'){
            newDigit+= str[i];
        }
    }
    return newDigit;
}
console.log(getDigits("abc8c0d1ngd0j0!8"));

function acronym(str){
    var newOut = "";
    var strSplit = str.split(" ");
    for(var i=0; i<=strSplit.length-1;i++){
        var word = strSplit[i]
        if(word.length > 0){
            newOut+= word[0]
        }
    }
    return newOut.toUpperCase();
}

console.log(acronym("Live from New York, it's Saturday Night!"));

function counNonSpaces(str){
    var arrayStr = str.split(" ");
    var newStr = arrayStr.join("")
    return newStr.length;
}
console.log(counNonSpaces("Hello world !"));

function removeShorterStrings(arr, minLength){
    var newArray = []
    for(var i = 0; i<arr.length; i++){
        var nonShortStr = arr[i];
        if(nonShortStr.length >= minLength){
            newArray.push(nonShortStr);
        }
    }
    return newArray;
}
console.log(removeShorterStrings(['There','is','a','bug','in','the','system'],3))

function longestCommonPrefix(strs){
    var firstWord = strs[0];
    for(var i = 1; i < strs.length; i++){
        while(strs[i].indexOf(firstWord) !== 0){
            firstWord = firstWord.substring(0 , firstWord.length-1);
            if (firstWord === ""){
                return "";
            } 
        }
    }
    return firstWord;
}

console.log(longestCommonPrefix(["flower","flow","flight"]));




