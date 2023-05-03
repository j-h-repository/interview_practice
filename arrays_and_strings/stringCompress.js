/*
Implement a method to perform basic string compression 
using the counts of repeated characters. 

For example, the string aabcccccaaa would become a2blc5a3.

If the "compressed" string would not become smaller than 
the original string, your method should return
the original string. 

You can assume the string has 
only uppercase and lowercase letters (a - z).


*/


//note on this approach:

const compressString= (string)=>{
    let compressed = []
    let count = 0

    for(let i=0; i<string.length; i++){
        count++;
        if(string[i+1]!=string[i]){
            compressed.push(string[i])
            compressed.push(count.toString())
            count=0
        }
    }
    return compressed.join("").length < string.length? compressed.join(""):string
}

let compressed1 = compressString("aabcaa")
console.log(compressed1)
let compressed2 = compressString("aabcccccaaa")
console.log(compressed2)

