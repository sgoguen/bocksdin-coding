const express = require('express'),
      app = express(),
      PORT = process.env.PORT || 3000,
      bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(require('./routes/todolist'));

app.listen(PORT);

console.log('api listening on: ', PORT);