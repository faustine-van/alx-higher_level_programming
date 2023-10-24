#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
const process = require('process');
const args = process.argv;
const id = parseInt(args[2]);

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const json = JSON.parse(body);
  for (const index in json.characters) {
    const character = json.characters[index];

    request(`${character}`, (err, res, body1) => {
      if (err) {
        console.log(err);
      }
      const jsonChar = JSON.parse(body1);
      console.log(jsonChar.name);
    });
  }
});
