#!/usr/bin/node
// title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const process = require('process');
const args = process.argv;
const url = args[2];
let count = 0;
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const json = JSON.parse(body);
  for (const key in json.results) {
    const url = json.results[key].characters;
    for (const index in url) {
      if (url[index] === person) {
        count += 1;
      }
    }
  }
  console.log(count);
});
