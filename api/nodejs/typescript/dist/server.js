require('dotenv').config();
const express = require('express'), app = express(), PORT = process.env.PORT || 3000, bodyParser = require('body-parser');
const swaggerUI = require('swagger-ui-express'), swaggerJsDoc = require('swagger-jsdoc');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(require('./routes/TodoList/routes'));
app.use((err, req, res, next) => {
    res.status(err.status || 500);
    res.json({ error: { status: err.status, message: err.message } });
});
const options = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'Todo List API',
            version: '1.0.0'
        },
        servers: [
            {
                url: `http://localhost:${PORT}`,
                description: 'Todo List API Documentation'
            }
        ]
    },
    apis: ['./dist/routes/**/*.js']
};
const specs = swaggerJsDoc(options);
app.use('/api-docs', swaggerUI.serve, swaggerUI.setup(specs));
app.listen(PORT);
console.log('api listening on: ', PORT);
