'use strict';

const { validate } = require('../../_utils');
const { createEntries, updateEntry, deleteEntry } = require('../../validation/validationSchema');

import { ICreateEntries, IUpdateEntry, IDeleteEntry } from "../../interfaces/validation";
import { IEntry } from "../../interfaces/todolist";

let todolistEntries: IEntry[] = [];

export default {
    getEntries: (): IEntry[] => {
        if (todolistEntries.length === 0)
            throw { status: 404, message: 'No entries found!' };
        
        return todolistEntries;
    },
    createEntries: (paramObj: ICreateEntries): IEntry[] => {
        validate(createEntries, paramObj);
    
        let newEntries = [], maxId = Math.max(...todolistEntries.map(entry => entry.id), 0);
        for (let entry of paramObj.entries) {
          maxId++;
          const newEntry = { id: maxId, ...entry };
          todolistEntries.push(newEntry);
          newEntries.push(newEntry);
        }

        return newEntries;
    },
    updateEntry: (paramObj: IUpdateEntry): IEntry[] => {
        validate(updateEntry, paramObj);
    
        for (let i = 0; i < todolistEntries.length; i++) {
          if (todolistEntries[i].id === paramObj.id) {
            todolistEntries[i] = { ...todolistEntries[i], ...paramObj.data };
            return [todolistEntries[i]];
          }
        }

        throw { status: 404, message: "Entry does not exist!" };
    },
    deleteEntry: (paramObj: IDeleteEntry): IEntry[] => {
        validate(deleteEntry, paramObj);

        todolistEntries = todolistEntries.filter(entry => entry.id !== paramObj.id);

        if (todolistEntries.length === 0)
            throw { status: 404, message: 'No entries remain!' }
        
        return todolistEntries;
    }
}