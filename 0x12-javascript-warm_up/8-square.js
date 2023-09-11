#!/usr/bin/node
//  prints a square
const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);

if (isNaN(num)) {
  console.log('Missing size');
}

for (let a = 0; a < num; a++) {
  console.log('X'.repeat(num));
}
