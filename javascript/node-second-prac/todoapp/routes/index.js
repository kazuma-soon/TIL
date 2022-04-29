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

/* GET home page. */
router.get('/', (req, res, next) => {
  const isAuth = req.isAuthenticated()
  
  if (isAuth) {
    const userId = req.user.id;
    client
      .query('SELECT * FROM tasks WHERE user_id = $1', [userId])
      .then(results => {
        res.render('index.ejs', { 
          title: 'Unko Zamurai',
          todos: results.rows,
          isAuth: isAuth,
        })
      })
      .catch(error => console.error(error.stack))
  }
  else {
    res.render('index', {
      title: 'ToDo App',
      isAuth: isAuth,
    })
  }
});

router.post('/', (req, res, next) => {
  client.query('SELECT $1::text as message', ['PG run!!'], (err, res) => {
  console.log(err ? err.stack : res.rows[0].message) // Hello World!
  })

  const todo = req.body.add;
  const userId = req.user.id;
  client
  .query('INSERT INTO tasks (user_id, content) VALUES ($1, $2)', [userId, todo])
  .then(results => {res.redirect('/')} )
  .catch(error => console.error(error.stack))
})

module.exports = router;
