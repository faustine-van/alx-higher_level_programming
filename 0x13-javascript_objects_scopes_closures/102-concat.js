#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const args = process.argv;
const arg1 = args[2];
const arg2 = args[3];
const arg3 = args[4];

// read fist args file
fs.readFile(arg1, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading ${arg1}: ${err.message}`);
    return;
  }

  fs.readFile(arg2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${arg2}: ${err.message}`);
      return;
    }
    const alldata = data + data2;

    fs.writeFile(arg3, alldata, (err) => {
      if (err) {
        console.error(`Error reading ${arg3}: ${err.message}`);
      }
    });
  });
});
