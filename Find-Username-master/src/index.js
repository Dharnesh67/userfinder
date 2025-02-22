const express = require('express');
const path = require('path'); 
const cors = require('cors'); 
const { ServerConfig } = require('./config');
const { UsernameRouter } = require('./routes');
const { ValidateUsername } = require('./middlewares');

const app = express();

// Enable CORS for frontend access
app.use(cors({ origin: "http://localhost:8080" })); 

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to parse JSON and URL-encoded requests
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/username', ValidateUsername.validateUsername, UsernameRouter);

// ✅ Corrected: Extract username from query parameters
app.get("/username/domain", (req, res) => {
    console.log("Query Params:", req.query); 
    const username = req.query.username; 
    if (!username) {
        return res.status(400).json({ error: "Username is required" });
    }
    res.json({ message: "Received username", username });
});

app.listen(ServerConfig.PORT, () => {
    console.log(`Successfully started the server on PORT : ${ServerConfig.PORT}`);
});
