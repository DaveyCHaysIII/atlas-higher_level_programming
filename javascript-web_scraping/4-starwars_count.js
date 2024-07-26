#!/usr/bin/node

const request = require('request');
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];

request(`${url}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  let filmCount = 0;
  const data = JSON.parse(body);
  for (const film of data.results) {
    if (film.characters.includes(wedge)) {
      filmCount++;
    }
  }
  console.log(filmCount);
});
