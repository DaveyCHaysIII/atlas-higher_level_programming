#!/usr/bin/node

const argv = process.argv[2];

const fs = require('node:fs');
fs.readFile(`${argv}`, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
