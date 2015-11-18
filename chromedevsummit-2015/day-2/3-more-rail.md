# More RAIL

## Using dev tools to profile awesomely

 * Say we are optiming load time
 * Use devtools to grab screenshots as page is visually changing
 * Find the "First Meaningful Paint"
 * Now look at everything before that, in the network pane, rightclick the column for "priority"
 * If you see something "low priority" you may want to know why - for example it may be have async flag
 * Focus on assets which matter, or block - Command click on filters for the stuff
     - XHR, JS, CSS, Font, Doc
 * Shift click an item to see relationships of asset dependencies
     - What caused what request?
     - Dig in on what is blocking the important requests to make first meaningful paint
 * Example "hoteltonight.com"
     - In dev tools, green is framerate
     - Measure from "touch" event to change in view
     - Better profiling from the timeline since it includes "(program)" as well, which is non-js time
     - Typically interested in the "self" column
     - in the demo they find a culprit of "captureStackTrace" which comes from a React module throwing errors
     - constructing Errors is expensive! - https://jsperf.com/new-error-vs-custom-error-object
     
     
     
 
