# JS and CSS - Parsha

### Why?
* CSS standard is weak
* Pre-processors can be buggy and even LESS/Sass have quirks/edge cases
* JS is standardized, and we understand it
    - Can extend it, generate it, etc...
    - Can modularize easily, using NPM to reuse style modules, or utility helpers

### How?
* Represent as json, use a "toCSS" method to convert it

### Why not? (My section)
* Because you can't hand it off to a designer
* Too much freedom, makes it harder to search



# Parallelism
* We should be harnessing the multicore power of modern machines
* Considerations include how we should handle shared memory and syntax
* Wait a year and reevaluate
    - Exploratory code in FF nightly
    - Google says they intend to eventually add it to chrome
