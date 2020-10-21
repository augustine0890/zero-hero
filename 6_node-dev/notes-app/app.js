const validator = require('validator');
const add = require('./utils');
const getNotes = require('./notes');


console.log(add(1, 2));
console.log(getNotes('This is a note.'));

console.log(validator.isEmail('augustine@example.com'));
console.log(validator.isEmail('augustine.com'));
console.log(validator.isURL('https://test.com'));
console.log(validator.isURL('augustine@example.com'));