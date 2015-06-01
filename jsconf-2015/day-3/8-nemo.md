# Nemo
Guy from Paypal talking about the switch to Node.JS after a team came over from netflix

### Why Nemo?
* Even great programmers let stuff through some time
* Selenium 
    - browser driver - json pipline - language driver
* After transformation, the tests were still in Java, even after the app switched to js
* Selenium webdriver sets up the toolsets necessary for controlling the browser
* Nemo wraps around the webdriver
    - it adds a plugin capability to add your own tools as necessary
### How?
* Need a test runner (mocha/cucumber/jasmine)
* Need a task runner (grunt/gulp)
* Uses "confit" to load a json configuration
    - NODE_ENV
    - shortstop - use 'env:x' as a value to a json attr which will be replaced with the env variable of x
    - To use this, you'd start with a main config file, and then a few other environment specific overrides
* Starts a selenium webdriver
* Initializes your plugins
    - webdriver abstractions
    - user interactions
    - proprietary functionality
    - Works by adding an attr (mixing in) to the nemo object
    
### Nemo View
* An example plugin that he created
* Auto gens a bunch of convenience functions that can help locate and interact with elements on the page
* Includes some "wait" functionality for async testing

### Locater Files
* After the app starts solidifying, you want to separate out the locaters from the test
* This next step makes the generic functions more "hard"
    
