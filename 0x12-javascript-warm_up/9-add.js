#!/usr/bin/node
// function add(a, b);
function add(a, b) {
  return a + b;
}
// prints the addition of 2 integers

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
const num1 = parseInt(args[3]);

console.log(add(num, num1));
