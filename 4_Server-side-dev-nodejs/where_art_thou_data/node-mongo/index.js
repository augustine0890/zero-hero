const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
const dboper = require('./operations');

const url = 'mongodb://localhost:27017';
const dbname = 'conFusion';


MongoClient.connect(url, {useUnifiedTopology:true}, (err, client) => {
    assert.strictEqual(err, null);
    console.log('Connected correctly to server');

    const db = client.db(dbname);
    dboper.insertDocument(db, { name: "Augustine", description: "Testing" }, 'dishes', (result) => {
        console.log('Insert Document:\n', result.ops);
        
        dboper.findDocument(db, 'dishes', (docs) => {
            console.log('Found Documents:\n', docs);
            
            dboper.updateDocument(db, { name: "Augustine" }, { description: "Updated Testing" }, 'dishes', (result) => {
                console.log('Updated Documents:\n', result.result);

                dboper.findDocument(db, 'dishes', (docs) => {
                    console.log('Found Documents:\n', docs);

                    db.dropCollection('dishes', (result) => {
                        console.log('Dropped Collection: ', result);
                        client.close();
                    });
                });
            });
        });
    });
});