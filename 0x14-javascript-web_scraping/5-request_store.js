#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const request = require('request');
request(argv[2]).pipe(fs.createWriteStream(argv[3]));
