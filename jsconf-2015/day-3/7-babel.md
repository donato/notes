# Javascript Transformation - Sebastian McKenzie
Works at CloudFlare

### History
* Wrote 6to5 as original project, but renamed to Babel as scope changed
* Scope changed into a more general js compiler
* Allows you to build things which will work even as js changes

### How ?
* Regex isn't powerful enough
* AST is just right
* Three pieces
    - Parser - creates the AST and passes to
    - Transformer - the brains of it
    - Generator - generates the new es5 code
   
### Transformer
* The magic happens while traversing the AST
* At any point of the traversal new nodes may be added or deleted
* Case Example 
    [x, y] = getCoords();
* You can do any kind of transformation, transpiling is just one

### Transpiling
* Example , arrow functions
    - implicit return for expressin
    - inherits arguments and this
    - cannot "new" it
        + We should error out in some new cases, so we can modify the construction to watch for it
        for example by adding an attr "_arrow" for arrow functions
        + not practical for now
    - No prototype
        + Not practical, could only be done by wrapping getters to not use a prototype
* What does this mean for us?
    - Don't learn from a transpiler
    - It may optimize by hoisting variables/methods which are reused
    - We can use htmlbars-inline-precompile to optimize using a transpiler
    - We should avoid the unspecified usages
    - Should not add functionality

### Browser Compatability
* We can actually improve compatability for IE8 by transforming named functions
* Watch out for IE8 named functions 
```js
( var e = function g() {}; e === g // not in IE8! )
```


### Emojis
* vars can be unicode characters, even representing emojis :)
