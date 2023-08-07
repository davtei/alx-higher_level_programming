$.getJSON(
  'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (data) {
    const charName = data.name;
    $('DIV#character').text(charName);
  }
);
