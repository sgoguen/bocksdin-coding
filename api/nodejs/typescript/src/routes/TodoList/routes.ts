'use strict';

const Router = require('express').Router;
const todolist = require("./model");

const router = module.exports = new Router();

/**
 * @swagger
 * definitions:
 *   entry:
 *     type: object
 *     properties:
 *       id:
 *         type: integer
 *       title:
 *         type: string
 *       due_date:
 *         type: string
 *   error:
 *     type: object
 *     properties:
 *       error:
 *         type: object
 *         properties:
 *           status:
 *             type: integer
 *           message:
 *             type: string
 */

/**
 * @swagger
 * /todolist/entries:
 *   get:
 *     tags: [todolist]
 *     description: Return all entries
 *     responses:
 *       200:
 *         description: Array of entries
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/definitions/entry'
 *       404:
 *         description: No Entries Found
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/definitions/error'
 */

router.get('/todolist/entries', async (req, res, next) => {
  try {
    const result = todolist.getEntries();
    res.json(result);
  } catch (error) {
    next(error);
  }
});

/**
 * @swagger
 * /todolist/entries:
 *   post:
 *     tags: [todolist]
 *     description: Create new entries
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               entries:
 *                 type: array
 *                 items:
 *                   type: object
 *                   properties:
 *                     title:
 *                       type: string
 *                       required: true
 *                     due_date:
 *                       type: string
 *                       required: true
 *     responses:
 *       200:
 *         description: Array of newly created entries
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/definitions/entry'
 *       400:
 *         description: Bad Request
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/definitions/error'
 */

router.post('/todolist/entries', async (req, res, next) => {
  try {
    const result = todolist.createEntries(req.body);
    res.json(result);
  } catch (error) {
    next(error);
  }
});

/**
 * @swagger
 * /todolist/entries/{id}:
 *   put:
 *     tags: [todolist]
 *     description: Update specific entry
 *     parameters:
 *       - in: path
 *         name: id
 *         description: id of existing entry
 *         schema:
 *           type: integer
 *         required: true
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               data:
 *                 type: object
 *                 properties:
 *                   title:
 *                     type: string
 *                   due_date:
 *                     type: string
 *     responses:
 *       200:
 *         description: Array with updated entry
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/definitions/entry'
 *       400:
 *         description: Bad Request
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/definitions/error'
 */

router.put('/todolist/entries/:id', async (req, res, next) => {
  try {
    req.body.id = parseInt(req.params.id);
    const result = todolist.updateEntry(req.body);
    res.json(result);
  } catch (error) {
    next(error);
  }
});

/**
 * @swagger
 * /todolist/entries/{id}:
 *   delete:
 *     tags: [todolist]
 *     description: Delete specific entry
 *     parameters:
 *       - in: path
 *         name: id
 *         description: id of existing entry
 *         schema:
 *           type: integer
 *         required: true
 *     responses:
 *       200:
 *         description: Array with remaining entries
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/definitions/entry'
 *       400:
 *         description: Bad Request
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/definitions/error'
 *       404:
 *         description: No Entries Remain
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/definitions/error'
 */

router.delete('/todolist/entries/:id', async (req, res, next) => {
  try {
    const result = todolist.deleteEntry(req.params);
    res.json(result);
  } catch (error) {
    next(error);
  }
});