const port = 3000;
const express = require("express");
const app = express();

app.get("/", (request, response) => {
    response.send("<h1>Hello Express.js!</h1>");
}).listen(port, () => {
    console.log(`The server has started and is listening on port number: ${port}`);
});
