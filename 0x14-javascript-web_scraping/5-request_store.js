#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const fs = require('fs');
  fs.writeFile(process.argv[3], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
