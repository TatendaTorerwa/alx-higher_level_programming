#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const { results } = JSON.parse(body);
    const count = results.reduce((acc, movie) => {
      return movie.characters.some(character => character.endsWith('/18/')) ? acc + 1 : acc;
    }, 0);
    console.log(count);
  }
});
