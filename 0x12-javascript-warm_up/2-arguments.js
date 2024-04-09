#!/usr/bin/node
// Print a message depending on number of arguments passed

const content = process.argv;
if (content.length === 2) {
  console.log("No argument");
} else if (content.length === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
