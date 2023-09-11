#!/usr/bin/node
//  prints a square
const process = require('process');
const args = process.argv;
const ac = args.length;

if (args.length <= 2) {
  console.log(0);
}
if (args.length === 3) {
  console.log(0);
}

let max = -Infinity;
for (let a = 0; a < ac; a++) {
  if (args[a] > max) {
    max = args[a];
  }
}
console.log(max);
