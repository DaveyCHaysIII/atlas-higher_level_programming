#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(`${url}`, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const result = {};
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    const user = `${data[i].userId}`;
    if (data[i].completed) {
      if (!result[user]) {
        result[user] = 0;
      }
      result[user] += 1;
    }
  }
  console.log(result);
});
