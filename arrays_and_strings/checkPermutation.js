/*
Given two strings, write a method to decide if one is a permutation of the other.
*/

//the function will account for spaces
function checkerWithSpace(stringOne, stringTwo){
    //split the string character-by-character
    //sort the array of characters
    //join them together to form a new string --> when comparing two identical arrays, the comparison was returning false
    let one = ((stringOne.split("")).sort()).join("") 
    let two = ((stringTwo.split("")).sort()).join("")

    console.log(one == two)
}

checkerWithSpace("apes", "peas")
checkerWithSpace("taco  cat", "attac co")

//the function will NOT account for spaces
function checkerNoSpace(stringOne, stringTwo){
    //split the string by spaces
    //join the characters with no space
    //split the string character-by-character
    //sort the array of characters
    //join them together to form a new string --> when comparing two identical arrays, the comparison was returning false
    let one = ((((stringOne.split(" ")).join("")).split("")).sort()).join()
    let two = ((((stringTwo.split(" ")).join("")).split("")).sort()).join()


    console.log(one == two)
}

checkerNoSpace("apes", "peas")
checkerNoSpace("taco cat", "attac co")