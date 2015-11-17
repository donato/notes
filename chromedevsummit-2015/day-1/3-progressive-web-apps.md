# Progressive Web Apps
Alex Russell & Andreas Bovins (Opera)

Big idea : The URL is the superpower of the Web, we should focus on it more.

## Context

Last year we talked about service workers, add-to-home, and push notifications!
All got shipped.

Again goal is to remove friction from user to product.
App store is a problem!
The web reduces friction to use like nothing ever
Users are not comfortable with apps because of
    1. Trust what they are doing
    1. Usage of space
    1. Requirements of privacy
    
The cost to get someone to try an add is $1 to $2, cost per loyal user is greater than $4

Each action to usage (step) is about a 20% drop off of customers
    * Go to store
    * Find in store
    * Click install
    * accept permissions
    * donload, wait
    * use it!
   
With a web app you can reduce it to 4 steps

Native-only does not work.
Many companies are actually discontinuing native development.

## Why do people keep using apps?
 * Offline usage
 * payments
 * re-engagment (push notifications)
 
 
## Implementation

There is a difference between a bookmark and a home app
We add the app to home screen, but bookmark pages within it
We need an "application shell" we think of it as an app if it can be used offline
Requirements
 * Needs to have a service worker
 * The start_url must use the service worker
 * Site must be a secure origin (TLS)
 * You must have visited the document twice over 5 minutes
 * Web Manifest
 

## Web manifest
Opera switched to the chromium/blink engine 3 years ago

 * Icons
 * Description
 * colors
 * related info
 
The manifest tells the browser how to make it work as a stand-alone.
You can specify things like "orientation:horizontal" or background color, etc..
 

## Debugging

 * Clear cache by clicking the flag > site-settings
 * New tab in chrome dev tools for service workers in chrome://inspect for devices
 * There's a chrome flag to enable to you to "enable add-to-shelf" or "disable engagement requirement" to help test
 * If you remove the URL bar, you need to 
     - add high-fidelity navigation
     - way to refresh for new content
     - New way to share (since you can't copy url from navbar) goo.gl//8pF0ca
 * onbeforeinstall Event, let's you cancel it until you are ready
 * Webapps aren't great for deep linking. They are working on it.
     
 
 
 
