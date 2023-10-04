# Typical Folder Structure for React

```
MY-APP
  > node_modules
  > public
  > src
    .gitignore 
    package-lock.json
    package.json
    README.md
```

### SRC Folder
`main folder where most of project code resides`
  - `index.js`    = entry point for react app
  - `App.js`      = root component that gets rendered in browser
  - `components`  = contains reusable and smaller components 
  - `pages`       = contains larger components that represent different pages or views
  - `styles`      = contains css/styling files including global styles and component specific styles
  - `assets`      = static assets such as images, icons, fonts used in application
  - `utils`       = utility functions or helper modules that are used throughout the project
  - `services`    = any services or API-related files

### PUBLIC Folder
`contains static assets that don't require processing, such as HTML file`

### NODE_MODULES Folder
`automatically created when you install dependencies`

### PACKAGE.json File
`lists the project's metadata and dependencies, including scripts for running various tasks`

### PACKAGE-LOCK.json File
`files automatically generated and lock the versions of installed dependencies ensuring consistent builds across machines`

### .GITIGNORE File
`specifies which files or directores should be ignored by version control`

### README.md File
`file containing general information about the project`