### Intro

### Installation
- `npm i typescript ts-node ts-node-dev @types/node @types/express`
- `npm i -g typescript ts-node`
- `tsc --init`

Hello and welcome back to another video.
In this video we will be setting up an existing NodeJS API to use Typescript.
Note, this will not be a how-to use Typescript, but rather how to setup a project to allow the use of Typescript.
First thing we need to do is install a few npm packages, ...1...
In order to use some commands in your terminal, such as tsc, you'll need to install typescript and ts-node globally, ...2...
Lastly, we'll run ...3... in order to generate a tsconfig.json file.

### tsconfig.json alterations
- allowJs: true
    - Uncomment this setting to allow normal JS files to compile
- outDir: "dist"
    - This will create a dist folder at the root of our project for the js output files that are built from our ts files
- strict: false
    - This allows us to build step by step into TS otherwise we would have lots of errors thrown for non-defined types and potential null values and the code would not compile to JS
- moduleResolution: "node"
    - Uncomment this setting to let tsc know this is a Node.js project
- include: ["src/**/*.js", "src/**/*.ts"]
    - This tells typescript to compile all our js files in our src folder
    - Located outside the compilerOptions object

Next we'll update our tsconfig.json with some quality of life changes.
We'll uncomment "allowJs" so normal JavaScript files we haven't converted yet will compile.
We'll set our "outDir" to "dist" to hold our compiled files.
We'll set "strict" to "false". This allows us to convert our application 
one file at a time without Typescript yelling about entire files not being typed.
We'll set "moduleResolution" to "node", this tells Typescript that this is a NodeJS project.
Lastly, we'll set "include" to compile all JavaScript and Typescript files located in our "src" folder.

### package.json
- start > `nodemon ./dist/server.js`
- postinstall > `tsc`
- dev > `ts-node-dev --respawn --transpile-only ./src/server.ts`

There are a few updates we need to make to our package.json file.
First the "start" script needs to point to our "dist" folder.
Next we'll create a "postinstall" script that runs "tsc" to compile our code
immediately after we run "npm install" in the future.
Lastly the "dev" script which will act as "nodemon" for the Typescript. The respawn flag enables hot-reloading,
and the transpile-only flag prevents the code being compiled into the dist folder for the time being.
This is to improve performance.

### create src
- move files
    - /routes
    - /validation
    - _utils.js
    - server.js
- update server.js
    - apis > ./src/routes/*.js
    - path is relative from root

The last thing we'll need to do before we're ready to develop using Typescript
is to create our "src" folder and move our relevant files into it.
Since we're using Swagger in this project, we'll also need to update our "files to watch"
in our "server.js" file. This "apis" path is relative from the root, not from the "server.js" file.

### joi-to-typescript
- `npm i joi-to-typescript`
- rename validation.js > validationSchema.ts
- mkdir ./src/interfaces
- ./src/generateValidationInterfaces.ts
- package.json
    - joiToTypescript > `ts-node ./src/generateValidationInterfaces.ts`
- run new script

As of right now you're free to start converting to Typescript.
Simply change the file extensions from "js" to "ts" and start adding type definitions.
However, since this particular project also uses "Joi" I'll show you how to generate interfaces
from the validation schema.
For that we'll need to install the "joi-to-typescript" package.
Next we'll make an "interfaces" folder inside our "src" directory. This will house the generated interfaces.
Next we'll create a script that will perform the conversion, so we'll add a new file called "generate validation interfaces"
in our "src" folder. ...4...
We'll create a package.json script to call our new file ...5...
And finally we'll run our new script and see the output.

### convert to typescript
- extension update only
    - _utils.js
- .src/interfaces/todolist.ts
    - IEntry
- mkdir ./routes/TodoList
    - model.ts
    - routes.ts
        - Remove utils and validation imports
        - Import model
        - Convert to using model methods
- server.ts
    - apis > "./src/routes/**/*.ts"