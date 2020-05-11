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
    }
  }
};
