#!/usr/bin/node
let first = -Infinity;
let second = -Infinity;
let number;
const argv = process.argv;

for (let i = 2; argv[i]; i++) {
  number = Math.floor(+argv[i]);
  if (number > first) {
    [first, second] = [number, first];
  } else if (number > second) {
    second = number;
  }
}
console.log(second !== -Infinity ? second : 0);
