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