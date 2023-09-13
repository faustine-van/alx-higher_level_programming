#!/usr/bin/node
/*
 - prints the number of arguments already printed and the new argument value
 - Prototype: exports.logMe = function (item)
 - Output format: <number arguments already printed>: <current argument value>
 */
let count = 0;

function logMe (item) {
  /* for (let a = 0; a < arguments.length; a++) {
     console.log(count + ':' + arguments[a]);
  }
  */

  console.log(`${count}: ${item}`);
  count++;
}
module.exports.logMe = logMe;
