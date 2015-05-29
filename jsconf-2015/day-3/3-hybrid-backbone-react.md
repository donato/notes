# The Hybrid Backbone & React App - Peter Piekarczyk
UI engineer from Trunk Club talking about the journey between frameworks
> @peterpme
> github.com/ppiekarczyk

### Getting Started
* They use coffeescript, but recommend babel instead
* Past dream stack - "brunch with panache" backbone chaplin jquery brunch coffeescript
    1. philosophy of "onion apps" so you can peel back abstraction as necessary
    2. numerous api calls and hydrations
    3. too many re renders
    4. Flame chart spikes
* Solution - replacing backbone views with React (reusable encapsulated components)
    * BWP = backend worker process
    * backenders are more comfortable working on the app
    * combine views and templates together
    * CSS is modeled after components 
        - 1 to 1 relationship between css and component

### Migration Process
    * you can start with 1 small component (a dropdown) and grow 
    * Use a Backbone/React mixin to share code across components
    
> At this point he goes through some code examples for react/backbone/chaplain


