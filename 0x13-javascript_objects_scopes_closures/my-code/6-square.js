#!/usr/bin/node

// a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

// You must use the class notation for defining your class and extends
// The constructor must take 1 argument: size
// The constructor of Rectangle must be called (by using super())
const OSquare = require("./5-square");

class Square extends OSquare {
  constructor(size) {
    super(size, size);
  }
  charPrint(c) {
    let printable = "C";
    if (c === undefined) printable = "X";
    for (let coloum = 0; coloum < this.height; coloum++) {
      let printcoloum = "";
      for (let row = 0; row < this.width; row++) {
        printcoloum += printable;
      }
      console.log(printcoloum);
    }
  }
}
module.exports = Square;
