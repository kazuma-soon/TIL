const express = require('express')
const app = express()
const port = 3000

const { Client } = require('pg')
const client = new Client({
  uesr: 'postgres',
  host: 'localhost',
  database: 'node_firstapp',
  port: 5432,
})
client.connect()

app.use(express.urlencoded({ extended: false }));

// トップページGET
app.get('/', (req, res) => {
  client
    .query('SELECT * FROM todos ORDER BY id desc')
    .then(results => {
      console.log('Selecting from todos...');
      res.render('index.ejs', { todos: results.rows })
    })
    .catch(error => console.error(error.stack));
})

// トップページPOST
app.post('/', (req, res) => {
  const content = req.body.content;

  client
    .query('INSERT INTO todos (content) values ($1)', [content])
    .then(results => {
      console.log('Connectiong table todos...');
      res.redirect('/');
    })
    .catch(error => console.error(e.stack))
})
  


app.listen(port);
