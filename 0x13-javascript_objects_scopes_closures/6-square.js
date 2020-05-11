#!/usr/bin/node
const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};
