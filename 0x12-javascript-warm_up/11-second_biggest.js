#!/usr/bin/node

const process = require('process');

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const a = process.argv.splice(2, process.argv.length - 2);

  let max = -Infinity;
  let second = -Infinity;

  for (const value of a) {
    const n = Number(value);

    if (n > max) {
      [second, max] = [max, n];
    } else if (n < max && n > second) {
      second = n;
    }
  }
  console.log(second);
}
