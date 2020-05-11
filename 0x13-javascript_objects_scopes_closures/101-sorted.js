#!/usr/bin/node
const dict = require('./101-data').dict;
const dict2 = {};
for (const value of Object.values(dict)) {
  dict2[value] = [];
}
for (const [key, value] of Object.entries(dict)) {
  dict2[value].push(key);
}
console.log(dict);
console.log(dict2);
