const express = require('express');
const router = express.Router();
const knex = require('../db/knex');
const bcrypt = require("bcrypt");

router.get('/', (req, res) => {
  const userId = req.session.userid;
  const isAuth = Boolean(userId);
  res.render('signin.ejs', {
    title: 'Sign in',
    isAuth: isAuth,
  })
})

router.post('/', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;
  const userId = req.session.userid;
  const isAuth = Boolean(userId);

  knex("users")
    .where({
      name: username,
    })
    .select("*")
    .then(async function (results) {
      if (results.length === 0) {
        res.render("signin", {
          title: "Sign in",
          errorMessage: ["ユーザが見つかりません"],
          isAuth: isAuth,
        });
      } else if (await bcrypt.compare(password, results[0].password)) {
        req.session.userid = results[0].id;
        res.redirect('/');
      } else {
        res.render("signin", {
          title: "Sign in",
          errorMessage: ["ユーザが見つかりません"],
          isAuth: isAuth,
        });
      }
    })
    .catch(function (err) {
      console.error(err);
      res.render("signin", {
        title: "Sign in",
        errorMessage: [err.sqlMessage],
        isAuth: false,
      });
    }); 
});

module.exports = router;
