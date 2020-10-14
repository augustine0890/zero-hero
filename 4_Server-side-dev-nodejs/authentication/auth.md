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
