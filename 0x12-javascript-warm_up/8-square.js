#!/usr/bin/node
const Number = Math.floor(+process.argv[2]);
let i = Number;

while (i > 0) {
  console.log('X'.repeat(Number));
  i--;
}
isNaN(Number) && console.log('Missing size');
