#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');
const url = process.argv[2];
const file = process.argv[3];
request(`${url}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  fs.writeFile(`${file}`, body, 'utf8', function (err) {
    if (err) {
      console.error(err);
    }
  });
});
