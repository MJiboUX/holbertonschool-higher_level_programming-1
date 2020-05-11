#!/usr/bin/node
const process = require('process');
const fs = require('fs');
let data = fs.readFileSync(process.argv[2], 'utf8');
fs.appendFileSync(process.argv[4], data);
data = fs.readFileSync(process.argv[3], 'utf8');
fs.appendFileSync(process.argv[4], data);
