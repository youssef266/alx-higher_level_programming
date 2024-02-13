#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let h = 0; h < this.height; h++) {
      let sum = '';
      for (let w = 0; w < this.width; w++) {
        sum += char;
      }
      console.log(sum);
    }
  }
}

module.exports = Square;
