const express = require('express');
const router = express.Router();

// pg -->
const { Client } = require('pg')
const client = new Client({
  user: 'postgres',
  database: 'todo_app',
  port: 5432,
})
client.connect()
// <--pg

router.get('/', (req, res, next) => {
  res.render('signup.ejs', { title: 'SignUp | Unko Zamurai' })
})

router.post('/', (req, res, next) => {
  const username = req.body.username;
  const password = req.body.password;
  const repassword = req.body.repassword;

  client
    .query('SELECT * FROM users WHERE name = $1', [username])
    .then(results => {
      if (results.rows.length > 0) { // パスワード使用済の場合
	res.render('signup.ejs', { 
	  title: 'SignUp | Unko Zamurai',
	  errorMessage: ['このユーザー名は使用できません']
	})
      } 
      if (results.rows.length === 0) {
	if (password === repassword) { // 正常な入力の場合
          client
	    .query('INSERT INTO users (name, password) VALUES ($1, $2)', [username, password])
	    .then(() => res.redirect('/'))
	    .catch(err => {
	      console.error(err)
	      res.render("signup", {
                title: "Sign up",
                errorMessage: [err.sqlMessage],
              })
	    })
        }
      }

    })
    .catch(err => {
      console.error(err);
      res.render("signup", {
        title: "Sign up",
        errorMessage: [err.sqlMessage],
      });
    })
})

module.exports = router;
