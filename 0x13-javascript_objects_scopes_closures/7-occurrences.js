#!/usr/bin/node
// a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map(e => e === searchElement && count++);
  return count;
};
