$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const addNew = $('<li></li>').text('New Item');
    $('UL.my_list').append(addNew);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
