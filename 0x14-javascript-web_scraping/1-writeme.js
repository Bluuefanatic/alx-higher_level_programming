#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Error: File path and content to write must be provided');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    console.log(`Successfully wrote to ${filePath}`);
  }
});
