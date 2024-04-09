#!/usr/bin/node
//prints two arguments passed to it

const args = process.argv;
let first = args[2];
let last = args[3];
console.log(first + " is " + last);
