#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`An error occurred. Status code: ${response.statusCode}`);
    return;
  }

  const completed = {};
  const tasks = JSON.parse(body);

  tasks.forEach(task => {
    if (task.completed) {
      completed[task.userId] = (completed[task.userId] || 0) + 1;
    }
  });

  console.log(completed);
});
