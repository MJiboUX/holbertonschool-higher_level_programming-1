#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error: ' + error);
    return;
  }
  console.log('code: ' + response.statusCode);
});
