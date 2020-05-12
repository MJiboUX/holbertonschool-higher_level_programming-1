#!/usr/bin/node
const process = require('process');
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, cont) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(cont);
});
