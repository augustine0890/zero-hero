# Networking Essentials
## Client and Server
- Web application are not stand-alone
- Many of them have a "Cloud" backend

```
                                                        THE CLOUD
Browser <--Client-server communication--> (Server Backend) <--> (Database)
                HTTP with REST API
```

- Network operations cause unexpected delays
- You need to write applications recognizing the asynchronous nature of communication
    - Data is not instantaneously available
- Hypertext Transfer Protocol (HTTP): a client-server communications protocol

## HTTP Response
- Server may send back data in a specific format:
    - eXtensible Markup Language (XML)
    - Javascript Object Notation (JSON)

## Node HTTP Module
- Core networking module supporting a high-performance foundation for a HTTP stack
- Using the module:
```javascript
const http = require('http');
```
- Creating a server:
```javascript
const server = http.createServer(function(req, res) {...});
```
- Starting the server:
```javascript
server.listen(port,...);
```
- Incoming request message information available through the first parameter "req"
```javascript
req.headers, req.body, ...
```
- Response message is contructed on the second parameter "res"
    - res.setHeader("Content-Type", "text/html");
    - res.statusCode = 200;
    - res.write("Hello World!");
    - res.end("<html></html>");

## Node fs Module
- Use fs module in your application
```javascript
const fs = require('fs');
```
- Some example fs methods:
```javascript
fs.exists(filePath, function(exists) {...});
```
