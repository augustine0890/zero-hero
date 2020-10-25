const fs = require('fs');

const book = {
    title: 'Ego is my Enemy',
    author: 'Ryan Holiday'
};

const bookJSON = JSON.stringify(book);
// console.log(bookJSON);
fs.writeFileSync('1-json.json', bookJSON);

// const parsedData = JSON.parse(bookJSON);
// console.log(parsedData.author);

// const dataBuffer = fs.readFileSync('1-json.json');
// const dataJSON = dataBuffer.toString();
// const data = JSON.parse(dataJSON);
// console.log(data.author);

const dataBuffer = fs.readFileSync('data.json');
const dataJSON = dataBuffer.toString();
const data = JSON.parse(dataJSON);
data.age = 29;

const userJSON = JSON.stringify(data);
fs.writeFileSync('data.json', userJSON);