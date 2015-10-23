#EmpireNode October 23, 2015


## How did we get here
- Rod Vagg
- Node.js Technical Steering Committee member
- Works at NodeSource -> bring node to enterprise customers

#### From v0.10 to v4.0

**The age of discontent, early 2014
Joyent (corporate stewardship)
Node-forward (use community resources to drive development)
together leads to the node-advisory board, where community members have some influence

It wasn’t enough.

** The great Leap
io.js, November-January end of 2014
io.js is created, a big forking of community

** The summer of convergence
io.js joins back into the community

-------------
overall they went with the “open governance” principle, using corporate PM’s, and corporate contributers as well.


#### Node.js LTS 
- https://medium.com/@nodesource/essential-steps-long-term-support-for-node-js-8ecf7514dbd#.6dskqths7
** LTS release
Goal - stability, predictability, build trust (this can be used for serious things)
Supported for 18 months + 12 months
** Stable release
come more often, every 6 months, will hold a stable version of V8, not upgraded except in major versions
** Canary
They do not want to confuse semver , so will probably use a -alpha or whatever

#### Major themes for next 12 months
better benchmarking
more stability
clarifiaction of core api
hardware
engagement
separation from V8




## The Importance of import and export
- Ben Newman (Meteor) benjamn

** We use eval all the time! 
Script tags
new Function()
require(‘vm’).runInThisContext(‘...’)
src of links

We can’t escape it, but commonjs can help tame it.

** Has CommonJS won? 
- from the perspective of node and npm, then yes!
Why does JS have a popularity contest? Other languages don’t! They just have a simple module system.

### Problems with CommonJS -
in web, loading the code is difficult (listen to Trek Glowacki)
dependency cycles
load order feels explicit but isn’t always
exports = module.exports
Multiple exports
very difficult to bundle without including tons of dead code

### Todays Solution
Self-discipline
	never assign to module.exports unless you are certain your module has no circular dependencies
store refecences to imported/exported (TODO// comeback)

### ES2015 Solution
All imports or “requires” are pointers to the most recently modified version of a globally shared var - https://github.com/benjamn/jsnext-skeleton


## A history of Data Science
JS was not an option for data analysis before node, because there was no file i/o!
js is a good option because the community is so huge, vibrant and ease of contribution
git is good for developers, but bad for domain experts
-- so she decided to build her own library, and chose node because
 * AbstractLEVELDown - interface for db operations
 * C integration


## Using Graph Theory to Build a Recommendation Engine in Node.js
- Keith Horwood [github](github.com/keithwhor)

Requirements
 * Recommend based off of listing OR user
 * Many reccomendations
 * clickbait
 * deliver in 2 weeks

** Solution **
Use a graph!
Nodes : Users and Listings
Edges : Requests, favorites, views (interactions)

Benefits of using a Graph
1. Node-type agnostic
1. Users generate recommendations for us
1. Graph traversals are fast - this is a BFS outwards

Technologies
[Neo4j](https://github.com/neo4j/neo4j) - biggest
pros - documented, just works
cons - ehh, its fine

Or build it yourself! [Nodal](github.com/keithwor/nodal)

[[ talks about making a graph class]]
pro's - simple
con's - it's all in memory

To get recommendations do a simple search using dijksra's algorithm, quitting when you have the desired number of recomendations
For example, grab 100 and store them as recommendations once per day. Then choose 3 random ones every time we want a recommendation.
Store the graphs on disk in case of server resets

