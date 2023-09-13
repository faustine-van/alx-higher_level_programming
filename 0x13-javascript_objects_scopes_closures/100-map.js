#!/usr/bin/node
//  imports an array and computes a new array
const list = require('./100-data.js').list;

const newArray = list.map((a) => a);
console.log(newArray);
const newArray1 = list.map((a) => a * list.indexOf(a));
console.log(newArray1);
