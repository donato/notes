# Headless Testing - Mike Ball
Guy is from Comcast and wants us to use Xvfb

### Why automated testing?
* Helps teams move quickly
* Helps understand how small changes propagate
* Insurance policy

### Why/how continuous integration
* Keeps the codebases health monitored
* Should happen many times per day
* Should be scientific, consistent, repeatable
* Should be fast and cheap


### State of headless testing
* PhantomJS is the leader, others are EnvJS, Rhino, RubyRacer
* What if your technology doesn't run in PhahtomJS?
    - Flash
    - NW.js -- both two are for making desktop apps using webtech
    - Google Polymer web component
    - VIDEO TAGS!


### Case Study on Google Polymer
* Virtualized CI don't have displays, or GUIs
* Current solutions
    - Travis CI - uses XVFB
    - SauceLabs uses selenium cloud
* But what if they don't work??? 
    - Budget, licensing, load is too great
* Then we need xvfb - x virtual frame buffer - a non-js tech that lets you run gui apps w/out a screen

### Sidebar : what is XVFB?
* X Video Server is a technology in Mac OS and linux that allows writing visual elements that can be interacted with
* Runs a server in memory instead of on hardware
* performs graphical operations in memory

### Back to Demo
* xvfb, ansible, chrome (w/ flash!), firefox, node, bower, web-component-tester
* Strategy
    - provision a vagrant ubuntu box
        + Vagrant is built on virtual box, it provides the linux VM, but it could also be on the cloud. It spins up lightweight headless VMs
    - use ansible (python) to install and configure
        + set xvfb onto display port 0
    - shell into the box (code : vagrant ssh)
        + clone down your demo
        + run your demo against display port 0
* You can use VNC to connect to the vagrant box, and see the test running
    - On the linux box install vnc server and run it on port 0

### What's next?
* spin up a cloud instance during your builds?
    - Maybe AWS, digital ocean, openstack?
* maybe headless functional testing is possible?

### Resources
* Demo : http://github.com/mdb/polymer-testing-box
* Demo : http://github.com/mdb/nw-testing-box

