if ($('HEADER').hasClass('green')) {
  $('DIV#toggle_header').click(function () {
    $('.green').toggleClass('red').removeClass('green');
  });
} else {
  $('DIV#toggle_header').click(function () {
    $('.red').toggleClass('green').removeClass('red');
  });
}
