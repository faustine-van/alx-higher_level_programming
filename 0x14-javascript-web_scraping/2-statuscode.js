#!/usr/bin/node
// display the status code of a GET request.
const request = require('request');
const process = require('process');
const args = process.argv;
const url = args[2];

request.get(url, (error, response) => {
  // Print the response status code if a response was received
  if (error) {
    console.error(error);
    return;
  }
  console.log('code: ', response.statusCode);
});
