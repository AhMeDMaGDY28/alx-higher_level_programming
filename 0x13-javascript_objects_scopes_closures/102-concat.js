#!/usr/bin/node
// a script that concats 2 files.
const fs = require('fs');

const firstFileContent = fs.readFileSync(process.argv[2]).toString();
const secondFileContent = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firstFileContent + secondFileContent);
