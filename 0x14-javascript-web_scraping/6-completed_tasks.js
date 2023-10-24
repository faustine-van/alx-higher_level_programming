#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
const process = require('process');
const args = process.argv;
const url = args[2];

const urlUser = 'https://jsonplaceholder.typicode.com/users';

request(urlUser, (err, res, body1) => {
  if (err) {
    console.log(err);
  }

  const jsonUser = JSON.parse(body1);
  const userCounts = {}; // Create an object to store user counts

  function processUser (index) {
    if (index < jsonUser.length) {
      const userId = jsonUser[index].id;
      let count = 0;
      const urlTodo = url + `?userId=${userId}`;

      request(urlTodo, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        const jsonTodo = JSON.parse(body);
        for (const number in jsonTodo) {
          if (jsonTodo[number].completed === true) {
            count += 1;
          }
        }
        userCounts[userId] = count; // store the counts for this user id
        processUser(index + 1); // move to next user
      });
    } else {
      console.log(userCounts);
    }
  }
  processUser(0); // // Start processing from the first user
});
