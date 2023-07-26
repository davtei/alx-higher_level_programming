#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + id, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const char = data.characters;
  for (const i of char) {
    request.get(i, function (error, response, body1) {
      if (error) {
        console.error(error);
      }
      const character = JSON.parse(body1);
      console.log(character.name);
    });
  }
});
