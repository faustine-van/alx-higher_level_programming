#!/usr/bin/node
//  imports an array and computes a new array
const list = require('./100-data.js').list;

// Create a new array with the same values as the original
const newArray = list.map((a) => a);
console.log(newArray);
/* Create a new array where each element is multiplied by its index
   in the original array
*/
const newArray1 = list.map((a, index) => a * index);
console.log(newArray1);
