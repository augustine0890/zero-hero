# Introduction to MongoDB
## Databases
- Databases are used to store structured information
- Databases support various operations on the data: query, insert, update, delete

## NoSQL Databases
- SQL (structured query language)
- Four broad categories:
    - Document databases (e.g., MongoDB)
    - Key-value databases (e.g., Redis)
    - Column-family databases (e.g., Cassandra)
    - Graph databases (e.g., Neo4J)

## Document Databases
- Document: A self-contained piece of information
- Collection: collection of documents
- Database: A set of collections

## Why NoSQL
- Scalability
    - Availability
    - Consistency
    - Partition tolerance
- Ease of deployment
    - No object-relation mapping required

## MongoDB
- Document Database
    - Server can support multiple databases
    - A database consists of a set of collections
    - A collection is a set of documents
    - Documnet is effectively a JSON document with some additional features

## Installing MongDB
**Install homebrew (https://brew.sh/) and run the following commands**
- `sudo chown -R $(whoami) $(brew --prefix)/*`
- `brew tap mongodb/brew`
- `brew install mongodb-community@4.4`

**aliases to set in your `zshrc` file**
- open your zshrc file
- `open ~/.zshrc`

**copy and paste shorcuts in the end of the file**
```
alias mongod='brew services run mongodb-community@4.4'
alias mongod-start='brew services start mongodb-community@4.4' #will start MongoDB automatically when you login into your Macbook
alias mongod-status='brew services list'
alias mongod-stop='brew services stop mongodb-community@4.4'
```
- Restart your terminal
- Type `mongod` in your terminal for run service & `mongod-stop` for finish it
- Test your mongodb connection with
`mongo`
`show dbs`

- Create a new database named `conFusion`
- `use conFusion`
- Create a collection named `dishes`
- `db.dishes`
- Delete (drop) collection named `dishes`
- `db.dishes.drop()`

[MongoDB Cheat Sheet](https://gist.github.com/bradtraversy/f407d642bdc3b31681bc7e56d95485b6)

## Mongoose ODM
- MongoDB stores data in the form of documents
- Object Data Model or Object Document Mapping or Object relational mapping (ORM)

## Mongoose Schema
- Schema: struture of the data to be stored
- Defines all the fields of your document and their types
- Schema types: String, Number, Date, Buffer, Boolean, Mixed, ObjectId, Array.
- Schema is used to create a Model function
- Schemas can be nested to enable supporting embedded or subdocuments