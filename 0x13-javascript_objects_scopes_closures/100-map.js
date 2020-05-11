#!/usr/bin/node
const list = require('./100-data').list;
let i = -1;
const map = list.map(function (x) {
  i++;
  return x * i;
}, i);
console.log(list);
console.log(map);
