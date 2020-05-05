#!/usr/bin/node

const process = require('process');

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (max < process.argv[i]) {
      max = process.argv[i];
    }
  }
  let second = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (second < process.argv[i] && process.argv[i] !== max) {
      second = process.argv[i];
    }
  }
  console.log(second);
}
