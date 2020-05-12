#!/usr/bin/node
const process = require('process');
const request = require('request');
request.get({url:'https://swapi-api.hbtn.io/api/films/' + process.argv[2]}, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
