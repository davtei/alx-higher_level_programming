#!/usr/bin/node
let args = 0;

exports.logMe = function (item) {
  console.log(args + ': ' + item);
  args++;
};
