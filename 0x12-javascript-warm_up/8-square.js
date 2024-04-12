#!/usr/bin/node
// a script that prints a square

// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square
// You must use console.log(...) to print all output
// You are not allowed to use var
// You must use a loop (while, for, etc.)

const printable = 'X';
if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2], 10);

  for (let index = 0; index < size; index++) {
    let rowContent = '';
    for (let index1 = 0; index1 < size; index1++) {
      rowContent += printable;
    }
    console.log(rowContent);
  }
}
