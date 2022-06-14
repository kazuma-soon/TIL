const passport = require("passport");
const LocalStrategy = require("passport-local");
const bcrypt = require("bcrypt");
const User = require("../models/user");

const cookieParser = require('cookie-parser');
const cookieSession = require("cookie-session");
const secret = "secretCuisine123";
// pg -->
const { Client } = require('pg')
const client = new Client({
  user: 'postgres',
  database: 'todo_app',
  port: 5432,
})
client.connect()
// <--pg

module.exports = function(app) {

  passport.serializeUser(function(user, done) {
    // 検証用ログ
    console.log("serializeUser");
    // req変数にアクセスできないので。以下でreq.session.useridをセット
    done(null, user.id);
  });

  passport.deserializeUser(async function(id, done) {
    // 検証用ログ
    console.log("deserializeUser");
    try {
      const user = await User.findById(id);
      done(null, user);
    } 
    catch (error) {
      done(error, null);
    }
  });

  passport.use(new LocalStrategy(
    // フォームから渡ってくる。この順番が重要。
    function(username, password, done) {
      // 検証用ログ
      console.log('Local Strategy called!');
      client
        .query('SELECT * FROM users WHERE name = $1', [username])
        .then(async function(results) {
	  if (results.rows.length === 0) {
	    return done(null, false, {message: "Invalid User"});
	  }
	  else if (await bcrypt.compare(password, results.rows[0].password)) {
            return done(null, results.rows[0]);
	  }
	  else {
	    return done(null, false, {message: "Invalid User"});
	  }
	})
        .catch(err => {
	  console.error(err);
	  return done(null, false, {message: err.toString()});
	})
    })
  )

  app.use(
    cookieSession({
      name: "session",
      keys: [secret],

      // Cookie Options
      maxAge: 24 * 60 * 60 * 1000, // 24 hours
    })
  );

  app.use(passport.initialize());
  app.use(passport.session());
} 


