#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

const x = argv[2];
const content = argv[3];

fs.writeFile(x, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
