if ($('.green').hasClass('green')) {
  $('#toggle_header').click(function () {
    $('.green').toggleClass('red').removeClass('green');
  });
} else {
  $('#toggle_header').click(function () {
    $('.red').toggleClass('green').removeClass('red');
  });
}
