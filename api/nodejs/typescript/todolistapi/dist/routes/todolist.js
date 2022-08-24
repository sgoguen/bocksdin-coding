'use strict';
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const Router = require('express').Router;
const router = module.exports = new Router();
const { validate } = require('../_utils');
const { createEntries, updateEntry, deleteEntry } = require('../validation/validation');
let todolistEntries = [];
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
router.get('/todolist/entries', (req, res, next) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        if (todolistEntries.length === 0)
            throw { status: 404, message: 'No entries found!' };
        res.json(todolistEntries);
    }
    catch (error) {
        next(error);
    }
}));
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
router.post('/todolist/entries', (req, res, next) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        validate(createEntries, req.body);
        let newEntries = [], maxId = Math.max(...todolistEntries.map(entry => entry.id), 0);
        for (let entry of req.body.entries) {
            maxId++;
            const newEntry = Object.assign({ id: maxId }, entry);
            todolistEntries.push(newEntry);
            newEntries.push(newEntry);
        }
        res.json(newEntries);
    }
    catch (error) {
        next(error);
    }
}));
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
router.put('/todolist/entries/:id', (req, res, next) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        req.body.id = parseInt(req.params.id);
        validate(updateEntry, req.body);
        for (let i = 0; i < todolistEntries.length; i++) {
            if (todolistEntries[i].id === req.body.id) {
                todolistEntries[i] = Object.assign(Object.assign({}, todolistEntries[i]), req.body.data);
                res.json([todolistEntries[i]]);
                break;
            }
        }
    }
    catch (error) {
        next(error);
    }
}));
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
router.delete('/todolist/entries/:id', (req, res, next) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        validate(deleteEntry, req.params);
        todolistEntries = todolistEntries.filter(entry => entry.id !== parseInt(req.params.id));
        if (todolistEntries.length === 0)
            throw { status: 404, message: 'No entries remain!' };
        res.json(todolistEntries);
    }
    catch (error) {
        next(error);
    }
}));
