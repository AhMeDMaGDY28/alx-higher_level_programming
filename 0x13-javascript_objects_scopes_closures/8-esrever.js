#!/usr/bin/node
// a function that returns the reversed version of a list:
exports.esrever = function (list) {
  const newArray = [];
  list.map(e => newArray.unshift(e));
  return newArray;
};
