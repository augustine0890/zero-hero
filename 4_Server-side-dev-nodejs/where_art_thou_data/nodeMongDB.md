# Node and MongoDB
## Node MongoDB Driver
- Provides a high-level API for a Node application to interact with the MongoDB Server
- Installation:
`npm install mongodb --save`
- The Node MongoDB driver supports several operations that can be performed from Node application:
    - Connecting to a MongoDB
    - Inserting, deleting, updating and querying documents

## Callback Hell
- Heavily nested callback code
    - Results from our tendency to write code top to bottom
    - Pyramid of doom
- Can use promises to tame it
    - Tries to preserve the top-down appearance of the code

## Promise
- Promise is a mechanism that supports asynchoronous computation
- Proxy for a value not necessarily known when the promise is created:
    - It represents a value that may be available now, or in the future, or never

`new Promise (function (resolve, reject) {...});`
- Solves the callback hell problem
- Promises can be chained
- Can immediately return:
    - Promise.resolve(result)
    - Promise.reject(error)

## Consuming Promises
- Comsumers of promise are notified of the fulfillment or rejection of the promise
    - Register the callbacks to handle fulfillment and rejection with the `.then()` --> can be chained
    - Use `.catch()` for handling errors
