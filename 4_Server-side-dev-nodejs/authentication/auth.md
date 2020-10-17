# Basic Authentication
## HTTP Basic Access Authentication
- Method for HTTP user agent to provide username and password with a request
- Server can challenge a client to authenticate itself
- Client needs to send the username and password in response

## Authorization Header
- The _Authorization_ header is constructed as follows:
    1. Username and password are combined into a string `"username:password"`
    2. The resulting string literal is then encoded using Base64.
    3. The authorization method and a space, i.e. "Basic" is then put before the encoded string.

## Cookies, Tea and err... Express Sessions
- HTTP Cookies: small piece of data sent from web server and stored on the client side
- Each subsequent request from the client side should include the _cookie_ in the request header
- Signed cookies: signed with a secret key on the server side
    - Digital signature with key-hash message authentication code (verifiable)
- Used to track user sessions
    - Combination of cookies with session id and server-side storage of information indexed by session id
    - Session information:
        - Stored by default in-memory (wiped out when server restarts)
        - Stored in permanent store on server side
        - Distributed session store if using multiple replicated servers
- Using cookies-parser
    - The _cookies-parser_ Experss middleware is already included in the Express REST API application
    - `npm install cookie-parser --save`

## Express Sessions
- `npm install express-session session-file-store --save`
