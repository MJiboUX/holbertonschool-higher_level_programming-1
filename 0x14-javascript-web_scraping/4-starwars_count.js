#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const list = JSON.parse(body).results;
  let n = 0;
  for (let i = 0; i < list.length; i++) {
    for (let j = 0; j < list[i].characters.length; j++) {
      if (list[i].characters[j].includes('18')) {
        n++;
      }
    }
  }
  console.log(n);
});
