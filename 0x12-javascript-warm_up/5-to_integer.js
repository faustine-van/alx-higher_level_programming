#!/usr/bin/node
/* prints My number: <first argument converted in integer>
   if the first argument can be converted to an integer: */

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(num);
}
