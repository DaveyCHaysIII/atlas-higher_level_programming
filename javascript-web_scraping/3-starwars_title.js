#!/usr/bin/node

const titleId = process.argv[2];
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${titleId}`, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const title = JSON.parse(body).title;
  console.log(title);
});
