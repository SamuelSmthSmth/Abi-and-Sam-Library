//Multiplication with two numbers

let add = function (x = 1,y = 1) {
  let result: number = x * y
  return result
}

let num1, num2: number;

num1 = 2
num2 = 4

console.log(`${add()} is the default answer`)
console.log(`${add(num1,num2)} is the answer using the variables`)

let userInput = prompt('Please enter your name: ');
console.log(`Oh so your name is ${userInput}...cool!`)