#!/usr/bin/node
// script that computes and prints a factorial

const process = require('process');
const args = process.argv;
const firstArg = parseInt(args[2]);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num <= 1) {
    return 1;
  }
  const res = num * factorial(num - 1);
  return res;
}
const result = factorial(firstArg);
console.log(result);
