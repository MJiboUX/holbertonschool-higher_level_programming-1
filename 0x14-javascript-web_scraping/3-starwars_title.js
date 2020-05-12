#!/usr/bin/node
const process = require('process');
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
