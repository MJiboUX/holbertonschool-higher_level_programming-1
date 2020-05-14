$(document).ready(function () {
  $('INPUT#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === '13') {
      const code = $('INPUT#language_code').val();
      const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + code;
      $.getJSON(url, function (data) {
        $('DIV#hello').html('<br />' + data.hello);
      });
    }
  });

  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + code;
    $.getJSON(url, function (data) {
      $('DIV#hello').html('<br />' + data.hello);
    });
  });
});
