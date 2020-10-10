const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
const dboper = require('./operations');

const url = 'mongodb://localhost:27017';
const dbname = 'conFusion';


MongoClient.connect(url, {useUnifiedTopology:true}).then((client) => {
    console.log('Connected correctly to server');
    const db = client.db(dbname);

    dboper.insertDocument(db, { name: "Augustine", description: "Testing" }, 'dishes')
        .then((result) => {
            console.log('Insert Document:\n', result.ops);
            return dboper.findDocument(db, 'dishes');
        })
        .then((docs) => {
            console.log('Found Documents:\n', docs);
            return dboper.updateDocument(db, { name: "Augustine" }, { description: "Updated Testing" }, 'dishes');
        })
        .then((result) => {
            console.log('Updated Documents:\n', result.result);
            return dboper.findDocument(db, 'dishes');
        })
        .then((docs) => {
            console.log('Found Update Documents:\n', docs);
            return db.dropCollection('dishes');
        })
        .then((result) => {
            console.log('Dropped Collection: ', result);
            return client.close();
        })
        .catch((err) => console.log(err));
})
.catch((err) => console.log(err));