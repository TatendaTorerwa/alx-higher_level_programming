#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const textContent = process.argv[3];

fs.writeFile(filePath, textContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(filePath);
});
