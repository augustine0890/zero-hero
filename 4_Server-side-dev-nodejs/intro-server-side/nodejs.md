# Introduction to Node.js and NPM
### Node JS
- JavaScript runtime built on Chrome V8 JavaScript Engine
- Uses an event-driven, non-blocking I/O model
    - Makes it lightweight and efficient

### Node Package Manager
- Node package manager (NPM): manages ecosystem of node modules/pakages
- A package contains:
    - JS files
    - package.json (manifest)

### Node Modules
- Each file in Node is its own module
- The _module_ variable gives access to the current module definition in a file
- The _module.exports_ variable determines the export from the current module
- The _require_ function is used to import a module
- File-based Modules
- Core Modules
    - Part of core Node
    - Example: path, fs, os, util,...
- External Node modules
    - Third-party modules
    - Installed using NPM
    - node_modules folder in your Node application
