#!/usr/bin/node

const path = process.argv[2];
const data = process.argv[3];

const fs = require('node:fs');
fs.writeFile(`${path}`, `${data}`,'utf-8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
});
