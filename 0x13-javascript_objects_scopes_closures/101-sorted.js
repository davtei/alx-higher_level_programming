#!/usr/bin/node
const dict = require('./101-data').dict;

const dictKey = Object.keys(dict);
const values = Object.values(dict);
let occ;
const newDict = {};
for (let i = 0; i < values.length; i++) {
  newDict[JSON.stringify(values[i])] = [];
  occ = dictKey.filter(key => dict[key] === values[i]);
  occ.forEach(item => newDict[JSON.stringify(values[i])].push(item));
}
console.log(newDict);
