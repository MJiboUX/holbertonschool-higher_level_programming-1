const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (data) {
  $.each(data.results, function (i, dict) {
    $('UL#list_movies').append(dict.title + '<br />');
  });
});
