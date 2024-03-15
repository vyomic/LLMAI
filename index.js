const express= require('express');
const ejs = require('ejs');
const pasth = require('path');
const bcrypt = require('bcrypt');
const app = express();
const collection = require('./config')
// ejs as view engine
app.engine('ejs', ejs.renderFile)
app.set('views', pasth.join(__dirname, 'views')); // Example path
app.use(express.json());
app.use(express.urlencoded({extended:false}));

// app.set('view engine', 'ejs');

app.get("/", (req,res)=>{
    res.render('login.ejs');
});
app.get("/signup", (req,res)=>{
    res.render("signup.ejs");
});
// register user
app.post("/signup", async(req, res)=>{
    const data ={
        name: req.body.email,
        password: req.body.password
    }
    const userdata = await(collection.insertmany(data));
    console.log(userdata)
})
const port = 5000;
app.listen(port, ()=> {
    console.log('server running on port:${port}');
})