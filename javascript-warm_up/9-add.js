#!/usr/bin/node
const argv = process.argv;
const numA = Number(argv[2]);
const numB = Number(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(numA, numB);
