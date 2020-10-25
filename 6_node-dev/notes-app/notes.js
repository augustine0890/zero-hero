const fs = require('fs');
const chalk = require('chalk');

const getNotes = function(note) {
    return note
};

const saveNotes = function (notes) {
    const dataJSON = JSON.stringify(notes);
    fs.writeFileSync('notes.json', dataJSON);
};

const loadNotes = function () {
    try {
        const dataBuffer = fs.readFileSync('notes.json');
        const dataJSON = dataBuffer.toString();
        return JSON.parse(dataJSON);
    } catch (err) {
        return []
    }
};

const addNote = function (title, body) {
    const notes = loadNotes();
    const duplicateNotes = notes.filter(function (note) {
        return note.title === title;
    })

    if (duplicateNotes.length === 0) {
        notes.push({
            title: title,
            body: body
        })
        saveNotes(notes);
        console.log(chalk.green.inverse('New note added!'));
    } else {
        console.log(chalk.red.inverse('Note title taken!'));
    }
}

const removeNote = function (title) {
    const notes = loadNotes();
    const removedNotes = notes.filter(function (note) {
        return note.title !== title;
    })
    if (removedNotes.length === notes.length) {
        console.log(chalk.red.inverse('The note is not exist'));
    } else {
        saveNotes(removedNotes);
        console.log(chalk.green.inverse('The note has removed'));
    }
}

module.exports = {
    getNotes: getNotes,
    addNote: addNote,
    removeNote: removeNote,
}