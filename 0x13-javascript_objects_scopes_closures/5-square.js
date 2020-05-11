#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((!Number.isInteger(w) || w === 0) ||
    !Number.isInteger(h) || h === 0) {

    } else if ((!Number.isInteger(w) || w < 0) ||
    (!Number.isInteger(h) || h < 0)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
};
