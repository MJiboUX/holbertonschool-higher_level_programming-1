#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((!Number.isInteger(w) || w === 0) ||
    !Number.isInteger(h) || h === 0) {

    } else if ((!Number.isInteger(w) || w < 0) ||
    (!Number.isInteger(h) || h < 0)) {

    } else {
      this.width = w;
      this.height = h;
      this.print = function print () {
        for (let i = 0; i < h; i++) {
          for (let j = 0; j < w; j++) {
            process.stdout.write('X');
          }
          process.stdout.write('\n');
        }
      };
    }
  }
};
