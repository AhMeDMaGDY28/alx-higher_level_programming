#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

let x = argv[2]
fs.readFile(x, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
