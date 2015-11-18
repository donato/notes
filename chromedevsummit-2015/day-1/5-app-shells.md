# App Shell + Service Worker
Instant loading apps

Remove the barrier of the "network" from getting content to your users screen.

## App Shell
This is a model for creating a webapp that can be used without a network connection
 html css, app.js
 
Events
  * Install
  * Activate
  * fetch event, or network event
  
Tools
  * sw-precache
  * sw-toolbox
  
## Demos
-- Not including the code --


# Web Push

## How it works
When a push request is received you have to go back to the apps website to find out what it really means.


## Best Practices
 * Use as few cycles as possible
 * Be wary that your notification is both Urgent and Important
 * Let them know what it's for before requesting permission
    - give them fine-grained control of types of notifications
 * Beware of duplication of notifications from app and webapp
 * Re-focus existing page instead of opening a new tab each time
 * Group notifications instead of spamming them (removel an old one and add a grouped one)
 * You can load the data for the app-click from the notificatino using an app-shell
 
## What's next?

 * Custom actions within the notification
    - Build an entire experience within the notification
    - Available in Chrome Dev
 * Payload - include serialized data in the push to reduce roundtrips