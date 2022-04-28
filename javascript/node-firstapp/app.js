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
  console.log('OK');
  client
    .query('SELECT * FROM todos ORDER BY id desc')
    .then(results => {
      console.log('Selecting from todos...');
      res.render('index.ejs', { 
        todos: results.rows,
        errors: [], 
      })
    })
    .catch(error => console.error(error.stack));
})

// トップページPOST
app.post('/', (req, res, next) => {  // validation
  const content = req.body.content;
  const errors  = [];
  if (content === '') {
    errors.push('contentを入力してください') 
  }  
  if (errors.length > 0) {
    console.log(errors);
    res.render('index.ejs', { 
      todos: [],
      errors: errors 
    });
  } else {
    next();
  }
}, (req, res) => {  // INSERT
  const content = req.body.content;

  client
    .query('INSERT INTO todos (content) values ($1)', [content])
    .then(results => {
      res.redirect('/');
    })
    .catch(error => console.error(error.stack))
})
  
// 新規登録ページ表示
app.get('/signup', (req, res) => {
  res.render('new.ejs');
})

// 新規登録機能
app.post('/signup', (req, res, next) => {
  const username = req.body.username;
  const email = req.body.email;
  const password = req.body.password;
  
  if (username === '' || email === '' || password === '') {
    res.redirect('/signup');
  } else {
    next();
  }
}, (req, res) => {
  const username = req.body.username;
  const email = req.body.email;
  const password = req.body.password;

  client
    .query('INSERT INTO users (name, email, password) values ($1, $2, $3)',
      [username, email, password])
    .then(results => {
      res.redirect('/');
    })
    .catch(error => console.error(error.stack))
}) 

// ログインページ表示
app.get('/signin', (req, res) => {
  res.render('signin.ejs');
})

// ログイン
app.post('/signin', (req, res, next) => {
  const email = req.body.email;
  const password = req.body.password;
  
  client
    .query('SELECT * FROM users WHERE email = $1', [email])
    .then(results => {
      if (results) {
        if (results.rows[0].password === password) {
          res.redirect('/');
        } else {
          res.render('signin.ejs');
        }
      } else {
        res.render('signin.ejs');
      }
    })
    .catch(error => console.error(error.stack))
})

app.listen(port);
