#!/usr/bin/node
const dict = require('./101-data').dict;

const total = Object.entries(dict);
const val = Object.values(dict);
const valsUniq = [...new Set(val)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in total) {
    if (total[k][1] === valsUniq[j]) {
      list.unshift(total[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
