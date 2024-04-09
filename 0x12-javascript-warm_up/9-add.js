#!/usr/bin/node
const first = Math.floor(+process.argv[2]);
const second = Math.floor(+process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(first, second);
