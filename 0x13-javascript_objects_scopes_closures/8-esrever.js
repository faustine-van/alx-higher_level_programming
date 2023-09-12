#!/usr/bin/node
// function that returns the reversed version of a list
function esrever (list) {
  const all = [];
  for (let a = list.length - 1; a >= 0; a--) {
    all.push(list[a]);
  }
  return all;
}
module.exports.esrever = esrever;
