// const validator = require('validator');
const chalk = require('chalk');
// const add = require('./utils');
// const getNotes = require('./notes');
const yargs = require('yargs');

// console.log(add(1, 2));
// console.log(getNotes('This is a note.'));

// console.log(validator.isEmail('augustine@example.com'));
// console.log(validator.isEmail('augustine.com'));
// console.log(validator.isURL('https://test.com'));
// console.log(validator.isURL('augustine@example.com'));

const error = chalk.inverse.bold.red;
const warning = chalk.keyword('orange');

// console.log(error('Error!'));
// console.log(warning('Warning!'));
// console.log(chalk.bold.green('Success!'));

// console.log(process.argv);

// Customize yargs version
yargs.version('1.1.0');

// add, remove, read, list
// Create add command
yargs.command({
    command: 'add',
    describe: 'Add a new note',
    builder: {
        title: {
            describe: 'Note title',
            demandOption: true,
            type: 'string'
        },
        body: {
            describe: 'Note body',
            demandOption: true,
            type: 'string'
        }
    },
    handler: function (argv) {
        console.log('Title: ' + argv.title);
        console.log('Body: ' + argv.body);
    }
});

// Create remove command
yargs.command({
    command: 'remove',
    describe: 'Remove the note',
    handler: function () {
        console.log('Removing the note')
    }
});

// Create list command
yargs.command({
    command: 'list',
    describe: 'List your notes',
    handler: function () {
        console.log('Listing out all the note')
    }
});

// Create read command
yargs.command({
    command: 'read',
    describe: 'Read a note',
    handler: function () {
        console.log('Reading a note')
    }
});

yargs.parse()
// console.log(yargs.argv);