#!/usr/bin/node

// a function that returns the reversed version of a list:
// Prototype: exports.esrever = function (list)
// You are not allow to use the built-in method reverse

exports.esrever = function (list) {
  const NewList = [];
  let NewIndex = 0;
  for (let OldIndex = list.length - 1; OldIndex >= 0; OldIndex--) {
    NewList[NewIndex] = list[OldIndex];
    NewIndex++;
  }
  return NewList;
};
