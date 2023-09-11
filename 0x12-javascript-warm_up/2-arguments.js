#!/usr/bin/node
/* prints a message depending of the number of arguments passed */
const process = require('process');
let args = process.argv;

if (args.length === 3){
  console.log('Argument found');
}else if (args.length > 3){
  console.log('Arguments found');
}else {
  console.log('No argument');
}
