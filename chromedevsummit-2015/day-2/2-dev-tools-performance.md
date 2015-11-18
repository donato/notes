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
 
