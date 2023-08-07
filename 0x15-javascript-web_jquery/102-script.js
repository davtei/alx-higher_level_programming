$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    $.get(
      'https://www.fourtonfish.com/hellosalut/hello/${code}',
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});
