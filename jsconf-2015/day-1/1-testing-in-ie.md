## Testing IE on Macbooks

Microsoft employee sharing some tools for making sure your websites work properly across IE and windows versions

### Why?

    * IE8 still has a big market share
    * Big corporations will not be switching off of IE8 due to exorbitant costs
        - Costs on the scale of millions for banks to get recertified w/ different version numbers
    * Luckily IE 11 is taking over market share from IE8/9/10
    * The next version, will be called IE edge 
        - will be heavily marketed win 10 will be given as a free upgrade, and will include Edge
        - will have 99% compatability with web standards


### How to test in Edge?
    * remote IE - uses a remote azure service to create a virtualized instance of ie on a specific browser
    * this may be an evolution of modern.ie

### Tools
    * get windows 10+IE-Edge here -> insider.windows.com
    * Ghostlab
    * Browser Stack
    * ngrok? lets you test local stuffs over a secure tunnel, to open it on a remote service (installs via homebrew)
    * vorlon.js
        - Why? Add debugging to browsers without it
       - add a script into a page, and it lets you debug something locally which is running remotely
    * Weinre - web inspector remote
    * dev.modern.ie
    * ngrok? lets you test local stuffs over a secure tunnel, to open it on a remote service (installs via homebrew)
    * edge team has a blog might be worth checking out
    * bit.ly/f12devtools

### What's next?
 * Headless version of IE - but not yet
 * script source debugging with remote IE



