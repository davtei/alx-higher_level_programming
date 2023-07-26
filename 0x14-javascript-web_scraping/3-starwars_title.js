#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const episode = process.argv[2];

request(url + episode, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const responseJSON = JSON.parse(body);
      console.log(responseJSON.title);
    } else {
      console.error('Error Code:', response.statusCode);
    }
  }
});
