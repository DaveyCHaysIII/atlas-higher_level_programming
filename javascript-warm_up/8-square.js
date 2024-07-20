#!/usr/bin/node
const argv = process.argv;
const num = Number(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('x');
    }
    process.stdout.write('\n');
  }
}
