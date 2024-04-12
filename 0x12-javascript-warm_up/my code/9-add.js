#!/usr/bin/node
// a script that prints the addition of 2 integers

// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)
// You must use console.log(...) to print all output
// You are not allowed to use var
function add(num1, num2) {
  return num1 + num2;
}

console.log(add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10)));
