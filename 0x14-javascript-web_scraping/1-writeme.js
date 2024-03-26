#!/usr/bin/node
const fs = require('fs');

  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
