#!/usr/bin/node
// searches the second biggest integer in the list of argument

const process = require('process');
const args = process.argv;

if (args.length <= 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  const sortArgs = args.sort(function (a, b) { return b - a; });
  console.log(sortArgs[3]);
}
/*
const ac = args.length;
let max = -Infinity;
for (let a = 0; a < ac; a++) {
  if (args[a] > max) {
    max = args[a];
  }
}
console.log(max);
*/
