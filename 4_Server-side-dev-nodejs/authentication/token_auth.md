# Token Based Authentication
## Cookies - Session Authentication
- Cookies set on the client side by the server
- Cookies used as a storage for session ID that is used as an index into server-side storage of session information

## Why Token-Based Authentication
- Session authentication becomes a problem when we need stateless servers and scalability
- Mobile application platforms hava a hardtime handling cookies/sessions
- Sharing authentication with other applications not feasible
- Cross-origin resource sharing (CORS) problem
- Cross-site request forgery (CSRF)

1. User requests access with their username and password
2. Server validates credentials
3. Server creates a signed token and sends it to the client
    - Nothing stored on the server
4. All subsequent requests from the client should include the token
5. Server verifies the token and responds with data if validated

## JSON Web Tokens
- Header (algorithm & token type) --> Payload (data) --> Signature

## jsonwebtoken Node Module
- `npm install jsonwebtoken --save`

## Passport-JWT
- Passport strategy for authenticating using JWT
- `npm install passport-jwt --save`
- Extracing the JWT from an incoming request
    - Header, body, URL Query parameter,...