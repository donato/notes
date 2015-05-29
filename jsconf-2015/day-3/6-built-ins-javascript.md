# Drawing Hands : Build ins written in javascript - John Dalton
Implementing parts or the whole of a language in the language itself

### Overview
* For example - [].indexOf ; which is different between mozilla and v8
    
* By using a subset of functionality you can get better performance than built-ins
    - You can even add features and still have better performance
    - You can optimize for common cases for your domain better than the general domain
    
* Intl
    - Good because writing it in js simplifies reading/understandably
    - Bad because of extra js functionality being exposed
    - Bad because of heavier boilerplate
    - Ugly: preventing tainting of js, testing, ensure correct stack behavior

* The good
    - Easy to develop
    - thus more contributions
    - Performance (inlining for free)
    - Experimental API
* The Bad and Ugly
    - No silver bullet for performance
    - "The hidden cost of javascript natives" - a talk in 2012 on a similar topic
    - We may have to write our own versions in order to get better performance than using the built ins
    
* Chakra - the js engine for IE-Edge
    - attempts to make built-ins more performant
    - optimize paths to ES6
    
