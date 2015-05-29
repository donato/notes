# Tungsten.js: Virtual DOM + Server Rendering in a Legacy Codebase - Andrew Rota
People from Wayfair.com discussing a way to bring virtual dom into a legacy code base of thousands of files

### Why?
* Performance - a 1 second app loses x% of customers
* Server side was pretty quick, client side was the bottleneck

### Room for improvement
1. jquery + backbone = slow DOM manipulation
    - Problem due to over-rendering, either updating when only parts change or when nothing changes
    - Problem due to overusing direct DOM manipulations
        + this.el.addClass('newclass')
    - We have to think about performance
        + $.empty() > $.html('');
2. Could have tried a rewrite - maybe use ember/angular/react?
    - Joel Spolsky - "The biggest mistake is to rewrite"
    - expensive, stop feature dev, breaking
3. Smart move is to work WITH the legacy code
    - Should respect that it grew organically with the right solution for the time
    - Will be using old framework/libraries
    - Has technical debt
    - **but overall it works**
    
### Wants
* Avoid DOM manipulation
    - easier debugging 
* Faster rendering

## Strategy
* ractive.js - used to precompile html templates to objects instead of strings
* mercury - rip out their virtual dom
* used backone to bind events and handle data layer
* wrote an integration library to bind it all (tungsten.js)

> You can't always build new telephone poles (infrastructure) 
  but you can use existing barbed wire fences to propagate the signal


### Resources
* [Tungsten.js](github.com/wayfair/tungstenjs)
* [dbmonster](https://github.com/wycats/dbmonster) - simulates a cluster/db monitoring system to test vdom performance
* [paperclip](http://paperclipjs.com/) - very fast vdom implementation
