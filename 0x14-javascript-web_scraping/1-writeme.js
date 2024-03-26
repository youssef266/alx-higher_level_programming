#!/usr/bin/node
const fs = require('fs');

const writeFile = (filePath, content) => {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
};
