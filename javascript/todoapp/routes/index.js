const express = require('express');
const router = express.Router();
const knex = require('../db/knex');
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
router.get('/', function (req, res, next) {
  const userId = req.session.userid;
  const isAuth = !!userId;
  knex("tasks")
    .select("*")
    .then(function (results) {
      res.render('index', {
        title: 'ToDo App',
        todos: results,
        isAuth: isAuth,
      });
    })
    .catch(function (err) {
      console.error(err);
      res.render('index', {
        title: 'ToDo App',
        isAuth: isAuth,
      });
    });
});

router.post('/', function(req, res, next) {
  const todo = req.body.add;
  const userId = req.session.userid;
  const isAuth = Boolean(userId);
  knex('tasks')
    .insert({ user_id: userId, content: todo })
    .then(function () {
      res.redirect('/');
    })
    .catch(function (err) {
      consle.error(err);
      res.render('index.ejs', {
        title: 'Unko Tabeta' 
      });
    });
});

router.use('/signup', require('./signup'));
router.use('/signin', require('./signin'));
router.use('/logout', require('./logout'));

module.exports = router;
