# Themes of 2015
Darren Fischer

## Trends

  * Big focus on WebView - specifically how auto-update keeps Chrome synched with WebView
  * Last year 400M users on chrome mobile, this year 800M users
  * mobile traffic is growing 2x faster than app traffic
  * avg user has about 25 apps - 80% of time spent on top 3
  * avg user visit about 100 different websites per month
     - low friction - no install necessary
     - There are more developers reaching people through sites than through apps
  * there is a much faster drop off in usage for second-tier apps than mobile devices

## Reliability *cough* Service Workers
 * Problem: don't assume a consistent network connection --this could be really cool for a video player--
 * Solution - service worker
 * See what The Guardian did -> when offline, provide a crossword puzzle instead of "no connection"
scale of service worker is 2.2B page loads/day, equal split desktop/mobile
  * New tab uses service worker too

## Performance
Responsive, each interaction immediately has a visual response.

 * R - Reaction time (100 ms)
 * A - Animation time (16.67 ms)
 * I - Idle time (Chunk it to less than 50ms of work)
 * L - Load time (Interactable within 1 second)

#### Projects for performance

 * AMP - static fast mobile apps
 * Polymer - enable easy dev
 * DevTools - and sharing on MDN

## Engagement
Get people into your page, and then bring 'em back.
 * "Add-to-Homescreen" for sites which use a service-worker which adds a link to site to home. 
 Now you get the fullscreen experience without the chrome menus.
 * Push notifications - allowing a website to push notifications to Chrome, who pushes it to device
 * Mobile first doesn't mean Native only
 * Auto-fill forms make a form 25% more likely to be submitted

**Progressive Web Apps**
Inspired by progressive enhancement. It still works on old browsers, but adds great features for 
whoever can use it.
