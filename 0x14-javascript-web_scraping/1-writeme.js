#!/usr/bin/node
// writes a string to a file.
// first argument file path and second argument is the string to write

const process = require('process');
const fs = require('fs');
const args = process.argv;
const file = args[2];
const string = args[3];

fs.writeFile(file, string, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
