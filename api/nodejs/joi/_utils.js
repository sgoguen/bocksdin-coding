'use strict';

module.exports = {
  dueDateRegExp: /^\d{2}\/\d{2}\/\d{4} at \d{2}:\d{2}(am|pm)$/,
  validate: (schema, objToValidate) => {
    const validation = schema.validate(objToValidate, { abortEarly: false });

    if (validation.hasOwnProperty('error')) {
      const message = validation.error.details.map(d => d.message).toString();
      throw { status: 400, message };
    }
  }
}