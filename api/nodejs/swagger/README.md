### `npm i swagger-jsdoc swagger-ui-express`

### server.js >
```
const swaggerUI = require('swagger-ui-express'),
      swaggerJsDoc = require('swagger-jsdoc');

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
  apis: ['./routes/*.js']
};

const specs = swaggerJsDoc(options);
app.use('/api-docs', swaggerUI.serve, swaggerUI.setup(specs));
```
### < server.js