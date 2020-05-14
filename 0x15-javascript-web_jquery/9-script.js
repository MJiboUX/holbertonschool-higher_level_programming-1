const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(url, function (data) {
  $('DIV#hello').html(data.hello);
});
