/*
Given a string, write a function to check if it is a permutation of a palin­ drome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
*/

/*

notes: 
    1. spaces are not accounted for
    2. palindromes can have 2 patterns
        a. an even number of letter pairs with one or no solo letters
*/




const isPalindrome =(string)=>{

    let regexPattern = /[^\W_]/ig //a regular express to grab only letters and numbers
    let filteredString = (string.match(regexPattern).join("")).toLowerCase() //a string containing what was found based on my regex filter

    let orderedString = (filteredString.split(" ").join("")).split("").sort() //convert the string into an array, then sort it
    let pairs = 0 //track pairs and solo count using numbers instead of arrays to save space
    let solo = 0
  
    let isPalindromeString = true

    for(let i=orderedString.length-1; i>-1; i--){ //start at the end of the array and decrement
        
        let placeHolder=orderedString[i] //grab the current char in the array
        if(placeHolder==orderedString[i-1]){ //if the current char is the same as the one before it
            pairs++ //increment the pairs count by 1
            i-- //decrement i by 1 so when the loop restarts, we skip over the just-read pair
        } else{
            solo++ //increment solo by 1 and allow the loop the decrement naturally
            if(solo>1){  //short circuit if the number of solos moves beyond 1
                return isPalindromeString=false
            }
        }
    }

    console.log(pairs, solo)

    if(pairs>=1 && solo<=1){ //if our palindrome pattern is met
        return isPalindromeString
    } else{
        return isPalindromeString=false
    }

    
    
}

console.log(isPalindrome("taco cat"))
console.log(isPalindrome("peter pan"))