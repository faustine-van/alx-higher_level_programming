#!/usr/bin/node
/* prints 3 lines: (like 1-multi_languages.js)
  but by using an array of string and a loop */
const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let a = 0;

while (lines[a]) {
  console.log(lines[a]);
  a++;
}
