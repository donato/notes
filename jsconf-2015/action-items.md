# Action Items

1. Make sure our purpose as a product is precise, well understood and prominent
1. Consultants are bringing tools/libraries to companies, we should have relationships with them
    - They can be more effective in promoting a good product than a sales team
1. See if we can benefit from a small virtual dom library 
    - trending today is paperclip (41kb) - the fastest
    - react (119kb) -  the most hyped
    - ractive (165kb) - the first
    - virtual-dom (5.8kb) - the smallest (aka the one we might use)
1. for visual diff comparison, try node-huxley
    - Huxley, was originally created by Facebook as a Python tool which was cancelled and deprecated
    - It was resurrected by open source community as node-huxley
1. "Optimistic update"
    - This is the idea that when someone makes an action, the UI should show it, even before the model updates
        + For example, you click "like" on facebook, and see the update, but the update hasn't propagated to servers yet
    - This is directly applicable to player actions against the chromecast
    - For more info check notes from Day 1 Facebook Relay
1. Mobile interaction
    - FastClick
    - Angular Mobile
1. App cache file
    - Allows an app to check for cache invalidation of all files simultaneously instead of independently
    - Could be a major win for mobile team
    
## Trends

1. Try eslint instead of jshint
    - It is more customizable and it is compatable with ES2015
    - It separates functional problems from stylistic ones
1. Server side rendering
    - Applicable to the portal team
    - send diffs of state to 
1. Microsoft is making a big push for Windows 10 (free upgrades for everyone)
    - New Microsoft browser is NOT "Spartan" it will be called "Edge"
    - Edge will use a jscript engine called "Chakra" instead of V8
        + Although this is even more fracturing, they aim to match standards
1. Serve different builds per user-agent
    - Optimize to include only the CSS prefixes needed, and only the shims neccessary
    - Smaller file size for everyone, faster load for flash fallback browsers
    - Negative is more complex build and deploy system
1. Web Components are getting closer, but still requires libraries which are mostly hacky
