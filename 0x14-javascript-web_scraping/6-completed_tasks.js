#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const data = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < data.length; i++) {
    dict[data[i].userId] = 0;
  }
  let j = 1;
  while (j < 11) {
    for (let i = 0; i < data.length; i++) {
      if (data[i].userId === j && data[i].completed === true) {
        dict[data[i].userId] += 1;
      }
    }
    j++;
  }
  let f = 0;
  for (const key in dict) {
    if (dict[key] !== 0) {
      f = 1;
    }
  }
  const d = {};
  if (f === 0) {
    return console.log(d);
  }
  console.log(dict);
});
