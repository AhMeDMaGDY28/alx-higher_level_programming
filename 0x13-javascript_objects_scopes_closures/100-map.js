#!/usr/bin/node
// a script that imports an array and computes a new array.
const data = require('./100-data').list;
console.log(data);
console.log(data.map((e, idx) => e * idx));
