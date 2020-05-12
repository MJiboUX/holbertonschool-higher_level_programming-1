#!/usr/bin/node
const process = require('process');
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  function (err, response, body) {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
