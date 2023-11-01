#!/usr/bin/node
/*
script that fetches the character name from this
URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
name must be displayed in the HTML tag DIV#character
- using Jquery
*/
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (person) {
      $('DIV#character').text(person.name);
    }
  });
});
