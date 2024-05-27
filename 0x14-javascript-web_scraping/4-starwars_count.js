#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const URL = argv[2];

request(URL, (err, _, body) => {
  if (err) return;
  const films = JSON.parse(body).results;
  const count = films.filter(film =>
    film.characters.some(url => url.includes('/18/'))
  ).length;
  console.log(count);
});
