'use strict';

const Router = require('express').Router;

const router = module.exports = new Router();

let todolistEntries = [];

router.get('/todolist/entries', async (req, res, next) => {
  try {
    res.json(todolistEntries);
  } catch (error) {
    next(error);
  }
});

router.post('/todolist/entries', async (req, res, next) => {
  try {
    let newEntries = [], maxId = Math.max(...todolistEntries.map(entry => entry.id), 0);
    for (let entry of req.body.entries) {
      maxId++;
      const newEntry = { id: maxId, ...entry };
      todolistEntries.push(newEntry);
      newEntries.push(newEntry);
    }
    res.json(newEntries);
  } catch (error) {
    next(error);
  }
});

router.put('/todolist/entries/:id', async (req, res, next) => {
  try {
    const id = parseInt(req.params.id);

    for (let i = 0; i < todolistEntries.length; i++) {
      if (todolistEntries[i].id === id) {
        todolistEntries[i] = { ...todolistEntries[i], ...req.body.data };
        res.json([todolistEntries[i]]);
        break;
      }
    }
  } catch (error) {
    next(error);
  }
});

router.delete('/todolist/entries/:id', async (req, res, next) => {
  try {
    todolistEntries = todolistEntries.filter(entry => entry.id !== parseInt(req.params.id));
    res.json(todolistEntries);
  } catch (error) {
    next(error);
  }
});