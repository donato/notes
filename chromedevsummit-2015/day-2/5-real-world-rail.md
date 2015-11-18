# Quantify and improve real-world RAIL
Ilya Grigorik

## Info from real users
 * App runs slower when it's sunny out
     - Because phone is mounted in the dashboard and it overheats
 * intro here:  bit.ly/perf-timing-primer
 * To optimize scrolling there should not be touch handlers - make them [passive](https://rbyers.github.io/EventListenerOptions/EventListenerOptions.html)
 * Use [event.timeStamp](http://www.w3schools.com/jsref/event_timestamp.asp)
 * Check with Performance observer
 
 
## How much work can we do in 16ms?
 * Depends on cpu/gpu
 * Depends on which core you're on
 * Is device in low-power state? Low battery?
 * Is the thermal regulator kicking in?
 * **We will never know!**
 
## PerformanceObserver
 * Can we track if we are losing frames?
 * w3c-github.io/frame-timing
 * Let the developers subscribe to find out if you are missing frames
 * PerformanceObserver
 
## IntersectionObserver
 * Investigate which part of page, or what is currently visible
 * https://rawgit.com/slightlyoff/IntersectionObserver/master/index.html
