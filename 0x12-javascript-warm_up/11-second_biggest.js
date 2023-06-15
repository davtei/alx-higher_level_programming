#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const num = process.argv.slice(2).map(Number);
  const large2 = num.sort(function (a, b) { return b - a; })[1];
  console.log(large2);
}
