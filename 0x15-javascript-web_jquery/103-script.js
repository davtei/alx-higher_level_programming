function translator() {
  const code = $('INPUT#language_code').val();
  $.get(
    'https://www.fourtonfish.com/hellosalut/hello/${code}',
    function (data) {
      $('DIV#hello').text(data.hello);
    }
  );
}

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    translator();
  });
});

$('INPUT#language_code').keypress(function (event) {
  if (event.keyPressed == 13) {
    translator();
  }
});
