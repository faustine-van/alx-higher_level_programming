#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const process = require('process');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const file = args[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(file, body, 'utf8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
