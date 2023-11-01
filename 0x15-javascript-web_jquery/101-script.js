#!/usr/bin/node
/*
script that adds a <li> element to a list
when the user clicks on the tag "DIV#add_item"
- The new element must be: <li>Item</li>
- The new element must be added to UL.my_list
- using Jquery
*/
$(document).ready(function () {
  // add class
  $('DIV#add_item').click(function () {
    $('UL.my_list').append($('<li></li>').text('Item'));
  });
  // remove class
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  // clear all classes
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
