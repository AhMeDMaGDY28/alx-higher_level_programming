#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments.

// You can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv;
let FirstBig = -Infinity;
let SecondBig;

if (!args[2]) {
  console.log(0);
  process.exit(0);
}
for (let index = 2; index < args.length; index++) {
  const temp = parseInt(args[index]);
  if (FirstBig < temp) {
    SecondBig = FirstBig;
    FirstBig = temp;
  }
}
if (SecondBig !== -Infinity) {
  console.log(SecondBig);
} else {
  console.log(0);
}
