#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('code: ' + response.statusCode);
});
