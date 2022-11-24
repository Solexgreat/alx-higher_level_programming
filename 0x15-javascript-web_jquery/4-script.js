const header = $('header');
$('div#toggle_header').click(function () {
  if (header.hasClass('red')) {
    header.removeClass('red').addClass('green');
  } else {
    header.removeClass('green').addClass('red');
  }
});
Footer
© 2022 GitH
