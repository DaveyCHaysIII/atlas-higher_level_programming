#!/usr/bin/node
const argv = process.argv;
let a = 0;
let b = 0;
let swap = 0;

for (let i = 2; i < argv.length; i++) {
  const number = Number(argv[i]);
  if (number > b) {
    b = number;
  }
  if (a < b) {
    swap = a;
    a = b;
    b = swap;
  }
}

console.log(b);
