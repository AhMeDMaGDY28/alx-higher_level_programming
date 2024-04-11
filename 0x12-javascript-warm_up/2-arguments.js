#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed:

// If no arguments are passed to the script, print “No argument”
// If only one argument is passed to the script, print “Argument found”
// Otherwise, print “Arguments found”
// You must use console.log(...) to print all output
// You are not allowed to use var
const args = process.argv;

if (args[3]) {
  console.log('Arguments found');
} else if (args[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
