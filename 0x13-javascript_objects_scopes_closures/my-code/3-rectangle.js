#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let coloum = 0; coloum < this.height; coloum++) {
      let printcoloum = "";
      for (let row = 0; row < this.width; row++) {
        printcoloum += "X";
      }
      console.log(printcoloum);
    }
  }
}
module.exports = Rectangle;
