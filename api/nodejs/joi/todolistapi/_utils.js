'use strict';

module.exports = {
  validate: (schema, objToValidate) => {
    const validation = schema.validate(objToValidate, { abortEarly: false });

    if (validation.hasOwnProperty('error')) {
      const message = validation.error.details.map(d => d.message).toString();
      throw { status: 400, message };
    }
  }
}