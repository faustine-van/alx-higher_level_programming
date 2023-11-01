#!/usr/bin/node
/*
script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello.
- using Jquery
*/
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
