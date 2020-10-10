const mongoose = require('mongoose');

const Dishes = require('./models/dishes');

const url = 'mongodb://localhost:27017/conFusion';
const connect = mongoose.connect(url, {
    useUnifiedTopology: true, 
    useNewUrlParser: true,
    useCreateIndex: true,
    useFindAndModify: false
});

connect.then((db) => {
    console.log('Connected to server!');
    Dishes.create({
        name: "Augustine",
        description: "Testing"
    })
    .then((dish) => {
        console.log(dish);
        return Dishes.findByIdAndUpdate(dish._id, {
            $set: { description: 'Updated test'},
        },{
           new: true
        }).exec();
    })
    .then((dish) => {
        console.log(dish);
        dish.comments.push({
            rating: 5,
            comment: 'Nice movie',
            author: 'Tom Hanks'
        });
        return dish.save();
    })
    .then((dish) => {
        console.log(dish);
        return Dishes.deleteMany({})
    })
    .then(() => {
        return mongoose.connection.close();
    })
    .catch((err) => {
        console.log(err);
    })
});