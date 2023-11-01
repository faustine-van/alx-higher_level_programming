#!/usr/bin/node
/*
script that fetches and prints how to say “Hello” depending on the language
- use this API service: https://www.fourtonfish.com/hellosalut/hello/
- language code will be the value entered
  in the tag INPUT#language_code (ex: es, fr, en etc.)
- translation must be fetched when the user clicks on INPUT#btn_translate
  and when press Enter
- translation of “Hello” must be displayed in the HTML tag DIV#hello
- using Jquery
*/
$(document).ready(function () {
  $('INPUT#btn_translate').on('keypress', function (e) {
    if (e.which === 13) {
      $('body').append("<p>You've pressed the enter key!</p>");
    }
  });
  $('INPUT#btn_translate').on('click', fetchTranslation);
  function fetchTranslation () {
    const lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

    $.ajax({
      type: 'GET',
      url,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
});
