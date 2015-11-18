# Introduction to RAIL
Paul Irish & Paul Lewis

The point of rail is to create a story based around users 
## Defining a performance baseline

 * Performance isn't necessarily linear from
     - Unbearable to bearable to good to great
 * ROI of investment decreases a lot from 500ms to 300ms
 * What is "too slow?"
     - is 50ms too slow?
     - It is for webgl or scroll, but not for page load
     - **The user context defines the required speed**
 * Let's talk about user perception
    - Break down user actions into atomic intentions
    
** Response **
 Buttons, form controls, anything that changes state
 100ms

** Animation **
 Scrolling, gestures, transitions
 people can detect changes in framework
 16ms
 
** Idle **
 Great time to do work, but have to be ready let an animation take over any time
 50ms
     
** Load **
 1000ms for users flow of thought
 -- Trick is to continue being responsive during the load --
 
 "Paul, Paul, Paul"
 
 
## Real world, Real RAIL
Things aren't so simple as you might like to believe

 * You can create a "RAIL Profile" ranking the importance of the different metrics.
 * For a content based site, Load might be the most important.
 * For an App you may worry about Animation and Idle the hardest
 * The other challenge is when you combine a tap that causes a load and animation!
     - Tapping on an article causes a --response-- a --load-- and then an --animation--.
     - Then again, maybe a response can actually be in the form of an animation.
 * Talk about the RAIL actions, and group them, choose which are primary

 
### Animation
 * Aim for 8 ms, because you have to share the 16ms with the browser
 * Do this by working with the compositor (ie, using opacity or transforms, because they don't trigger layout)
 * For animation try FLIP ( First, Last, Invert, Play)
     - Find dimensions, add class to move it to the final location, get dimensions again
     - then apply a transform to translate and scale it, BETTER PERFORMANCE (not intuitive)
     - This works because you put the heavy work into the 100ms of "response" and then its more porformant
       for the "animation"
 * Don't do animations during scrolls
 
### Idle
 * You generally have to guess if you're idle or not
 * Chrome 47 introduces requestIdleCallback
    - Given a "deadline" object which can tell you how much time is remaining
 * Do non-essential work here (maybe analytics pings)
 
### Load
 * Focus on reaching 1000ms for the top 75% of internet users
 * Inline "app-shell" css, lazyload rest
 * http://www.html5rocks.com/en/tutorials/webcomponents/imports/ 
 * http://webcomponents.org/articles/introduction-to-html-imports/
 
### Smoke Test
 * [webpage test](http://www.webpagetest.org/)
 * get a timeline object
 * put it into [Big Rig](https://github.com/GoogleChrome/big-rig)
