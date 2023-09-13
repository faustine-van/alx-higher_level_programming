#!/usr/bin/node
// script that prints x times “C is fun”

const process = require('process');
const args = process.argv;
const firstArg = parseInt(args[2]);

for (let a = 0; a < firstArg; a++) {
  console.log('C is fun');
}
