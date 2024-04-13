#!/usr/bin/node
const Number = Math.floor(+process.argv[2]);
function rec (num) {
  return num ? num * rec(num - 1) : 1;
}
console.log(rec(Number));
