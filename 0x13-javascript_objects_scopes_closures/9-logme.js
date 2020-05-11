#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
  function count (i) {
    console.log(i + ': ' + item);
  }
  count(i);
  i++;
};
