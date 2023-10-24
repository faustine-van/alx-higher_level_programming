#!usr/bin/node
// reads and prints the content of a file.

const process = require('process');
const fs = require('fs');
const args = process.argv;
const file = args[2];

fs.readFile(file, 'utf8', (error, content) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(content);
});
