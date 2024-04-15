#!/usr/bin/node

// a function that returns the number of occurrences in a list:
// Prototype: exports.nbOccurences = function (list, searchElement)

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let index = 0; index < list.length; index++) {
    const element = list[index];
    if (element === searchElement) {
      num++;
    }
  }
  return num;
};
