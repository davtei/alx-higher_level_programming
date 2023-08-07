$.getJSON(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    const movies = data.results;

    movies.forEach(function (movie) {
      const movieList = $('<li></li>').text(movie.title);
      $('UL#list_movies').append(movieList);
    });
  }
);
