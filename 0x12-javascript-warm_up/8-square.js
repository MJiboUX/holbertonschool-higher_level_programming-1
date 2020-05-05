#!/usr/bin/node

const process = require('process');

if (process.argv.length < 3) {
  console.log('Missing size');
} else if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  const a = [parseInt(process.argv[2])];

  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    a[i] = [parseInt(process.argv[2])];
  }

  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      a[i][j] = 'X';
    }
    a[i] = a[i].join('');
  }
  console.log(a.join('\n'));
}
