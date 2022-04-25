const express = require('express');
const router = express.Router();
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  password: '0141',
  database: 'todo_app'
});

connection.connect((err) => {
  if (err) {
    console.log('error connecting: ' + err.stack);
    return;
  }
  console.log('success');
});

/* GET home page. */
router.get('/', function(req, res, next) {
  connection.query(
    'select * from tasks;',
    (error, results) => {
      console.log(error);
      console.log(results);
      res.render('index.ejs', {
        title: 'Unko Taberu',
        todos: results  
      })
    }
  );
});

router.post('/', function(req, res, next) {
  const todo = req.body.add;
  connection.query(
  'insert into tasks (user_id, content) values (?, ?);',
  [1, todo],
  (error, results) => {
    console.log(error);
  })
  res.redirect('/');
});

module.exports = router;
