#!/usr/bin/node

$('document').ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    data.results.forEach(function (film) {
      $('#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
