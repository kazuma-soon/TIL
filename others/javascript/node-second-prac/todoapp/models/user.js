// pg -->
const { Client } = require('pg')
const client = new Client({
  user: 'postgres',
  database: 'todo_app',
  port: 5432,
})
client.connect()
// <--pg

const TABLE_NAME = "users";

async function findById(userId) {
  const user = await where(userId);
  if (user === null) {
    throw new Error('User not found')
  }
  return { ...user };
}

async function where(condition) {
  return await client
                 .query('SELECT * FROM users WHERE id = $1', [condition])
                 .then(results => {
		   if (results.rows.length === 0) {
		     return null;
		   }
		   console.log(results.rows[0]);
		   return results.rows[0];
		 });
}

module.exports = {
  findById,
};
