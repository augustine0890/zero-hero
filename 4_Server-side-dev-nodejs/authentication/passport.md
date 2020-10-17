# Authentication with Passport
## Passport
- Authentication middleware for Node.js
- Modular, flexible
- Supports various strategies for authentication:
    - Local strategy
    - OpenID
    - Oauth (Facebook, Twitter, G+ etc.) single sign-on
- Supports sessions (optional)
- Installing: `npm install passport --save`

## Passport-Local
- Passport strategy for authenticating a user with a username and password
- Installing: `npm install passport-local --save`

## Passport-Local-Mongoose
- Mongoose plugin to simplify building username and password login
- Intalling: `npm install passport-local-mongoose --save`
- Makes available Mongoose schema support for managing users
- Adds Username, hash ans salt field to store the username, the hashed password ans the salt value
- Additional methods to the User schema to support passport local authentication