require('dotenv').config();

const express = require('express'),
      app = express(),
      PORT = process.env.PORT || 3000,
      bodyParser = require('body-parser');

      
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(require("./routes/todolist.js"));

app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.json({ error: { status: err.status || 500, message: err.message }});
});

app.listen(PORT);

console.log('api listening on: ', PORT);