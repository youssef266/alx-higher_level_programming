#!/usr/bin/node
// script.js
const initialList = require('./100-data');

// Use map to create a new list with each value multiplied by its index
const newList = initialList.map((value, index) => value * index);

// Print the initial list
console.log('Initial List:', initialList);

// Print the new list
console.log('New List:', newList);
