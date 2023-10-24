#!/usr/bin/node
// title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const process = require('process');
const args = process.argv;
const id = parseInt(args[2]);

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
