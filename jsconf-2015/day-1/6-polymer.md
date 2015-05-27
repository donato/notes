# Polymer - the future of web components
Polymer is sort of syntactic sugar to webcomponents that Google started, that Comcast has been using for a few years

Hard to follow along due to using jsfiddle which had a small font

### Web Components
    1. <template>'s - allows you to parse data without putting it into the DOM
    1. imports - load templates from other html pages?
    1. Shadow DOM - styles don't bleed outside of the elements
    1. custom elements - var customTag = Object.create(HTMLElement.prototype);
    
    Can pass params/args into it
    
### Polymer
    * Easier to generate custom objects with shadow roots
    * Allows data-binding
    * Allows interaction, using a custom syntax for example on-click on-tap on-___
    * Makes reuse better! 
        - first time you can package js/css/html together
        
### Big Ideas
    * Each page in a tabbed website is a web component
    
### Challenges
    * Only chrome allows it
    * How to test? Web component tester
    * how to include files? momentjs
    * how to share code among components - for example a logger?
    * cache busting
    * Chromecast doesn't support IE9
    * New releases of polymer are breaking

