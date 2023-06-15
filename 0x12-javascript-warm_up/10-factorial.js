#!/usr/bin/node
function factorial (f) {
  if (f === 0 || isNaN(f)) {
    return 1;
  }
  return f * factorial(f - 1);
}
const f = parseInt(process.argv[2]);
console.log(factorial(f));
