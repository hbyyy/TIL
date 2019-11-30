const express = require('express');
const app = express();

// 이 폴더를 루트 폴더로 정할 것이다
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.get('/todos', (req, res) => {
    const todos = [
        { id : 1, content: 'HTML', completed: false},
        { id : 2, content: 'CSS', completed: true},
        { id : 3, content: 'javascript', completed: false}
    ];


    res.send(todos);
});

app.listen(5002, () => console.log('Server is running on port 5002!'));


