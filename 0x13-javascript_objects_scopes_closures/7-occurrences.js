#!/usr/bin/node
// function that returns the number of occurrences in a list

function nbOccurences (list, searchElement) {
  let i = 0;
  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      i++;
    }
  }
  return i;
}
module.exports.nbOccurences = nbOccurences;
