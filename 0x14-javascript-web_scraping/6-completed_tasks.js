#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
const process = require('process');
const args = process.argv;
const url = args[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const jsonTodo = JSON.parse(body);
  const userCounts = {}; // Create an object to store user counts

  for (const todo of jsonTodo) {
    if (todo.completed) {
      const userId = todo.userId;
      userCounts[userId] = (userCounts[userId] || 0) + 1;
    }
  }
  console.log(userCounts);
});
