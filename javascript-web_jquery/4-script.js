#!/usr/bin/node

$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').addClass('green').removeClass('red');
    }
  });
});
