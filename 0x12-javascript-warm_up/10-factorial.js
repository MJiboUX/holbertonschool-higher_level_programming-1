#!/usr/bin/node

function fact (n) {
  if (n === 0) {
    return (1);
  } else {
    return (n * fact(n - 1));
  }
}

const process = require('process');

console.log(fact(parseInt(process.argv[2], 10) || 0));
