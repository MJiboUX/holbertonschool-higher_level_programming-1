$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + code;
    $.getJSON(url, function (data) {
      $('DIV#hello').html('<br />' + data.hello);
    });
  });
});
