#!/usr/bin/node
/*
script that adds the class "red" to the <header>
element when the user clicks on the tag "DIV#red_header"
- using Jquery
*/
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
