'use strict';
const Joi = require('joi');
const dueDateRegExp = /^\d{2}\/\d{2}\/\d{4} at \d{2}:\d{2}(am|pm)$/;
module.exports = {
    createEntries: Joi.object({
        entries: Joi.array().items(Joi.object({
            title: Joi.string().required(),
            due_date: Joi.string().pattern(dueDateRegExp).required()
        })).min(1).required()
    }).required()
        .meta({ className: "ICreateEntries" }),
    updateEntry: Joi.object({
        id: Joi.number().integer().min(1).required(),
        data: Joi.object({
            title: Joi.string().optional(),
            due_date: Joi.string().pattern(dueDateRegExp).optional()
        })
            .or('title', 'due_date')
            .required()
    }).required()
        .meta({ className: "IUpdateEntry" }),
    deleteEntry: Joi.object({
        id: Joi.number().integer().min(1).required()
    }).required()
        .meta({ className: "IDeleteEntry" })
};
