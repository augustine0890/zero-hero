# Introduction to Express
- Fast, unopinionated, minimalist web framework for Node.js
- Third-party _middleware to extend functionality
- Installing Express: `npm install experess --save`
- Middleware provide a lot of plug-in functionality that can be used within your Express application

## Representational State Transfer (REST)
### Web Services
- A system designed to support interoperability of systems connected over a network
    - Service oriented architecture (SOA)
    - A standardized way of integrating web-based applications using open standards operating over the Internet
- Two common approaches used in practice:
    - SOAP (Simple Object Access Protocol) based services
        - Uses WSDL (Web Services Description Language)
        - XML based
    - REST (Reprensentational State Transfer)
        - Use Web standards
        - Exchange of data using either XML or JSON
        - Simpler compared to SOAP, WSDL etc.
### REST
- Four basic design principles:
    - Use HTTP methods explicitly
    - Be stateless
    - Expose directory structure-like URIs
    - Transfer using XML, Javascript Object Notation (JSON), or both
- Nouns (Resources): _unconstrained_
- Verbs: _constrained_, GET, PUT, POST, DELETE
- Representations: _constrained_, XML, JSON

### HTTP GET
- Used by clients to request for information
- Issuing a GET request transfers the data from the server to the client in some representation (XML, JSON)

### HTTP PUT, POST, DELETE
- HTTP PUT updates a resource
- HTTP POST creates a resource
- HTTP DELETE removes the resource identified by the URI

### Stateless Server
- Server side should not track the client state:
    - Every request is a new request from the client
- Client side should track its own state:
    - E.g., using cookies, client side database
    - Every request must include sufficient information for server to serve up the requested information
    - Client-side MVC setup

### Express Router
- Express supports this through `app.all`, `app.get`, `app.post`, `app.put`, `app.delete` methods.
- Application Routes:
    - `app.all('/dishes', function(req,res,next) {...})`
    - `app.get('/dishes', function(req,res,next) {...})`
    - `app.post('/dishes', function(req,res,next) {...})`
    - `app.put('/dishes', function(req,res,next) {...})`
    - `app.delete('/dishes', function(req,res,next) {...})`

### Body Parser
- Middleware to parse the body of the message
- Using Body Parser:
```javascript
var bodyParser = require('body-parser');
app.use(bodyParser.json()); // parse the JSON in the body
```
    