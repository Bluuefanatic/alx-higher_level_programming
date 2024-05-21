#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Error: URL must be provided');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    process.exit(1);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
