#!/usr/bin/node

const request = require('request');
const wedgeId = '18';
const url = process.argv[2];

request(`${url}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  let filmCount = 0;
  const data = JSON.parse(body);
  for (const film of data.results) {
    for (const character of film.characters) {
      if (character.includes(wedgeId)) {
        filmCount++;
      }
    }
  }
  console.log(filmCount);
});
