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


## Making front-end modules actually work
[Lin Clark](twitter.com/LinClark)

***Module Shaming*** - Do webpack people even know what modular is?
Should npm packages and github repos have a 1-to-1 mapping?
Modular doesn't necessarily mean "reusable chunks of code" or even "not labeled for individual sale"

Modularity is more about "readability" and creating cognitive chunks, than about re-usability.

Alternative ideas used to define modularity :
cohesion - getter/setter on a model, belong together
coupling - degree of interdependence between modules

We want to maximize cohesion and minimize coupling. But we don't actually care about re-usability, even though it is a possible perk.

In an html file you can mark dependencies for scripts, but not between scripts. Well maybe you could, but you wouldn't want to!

In webpack/browserify, you can

browserify - transpiler
webpack - loaders > is this still modular?

Maybe not, but in webpack you can create "intermediary modules" using a feature called "libraries" and using externals.

webpack can decouple css class names using ["local:"](https://medium.com/seek-ui-engineering/the-end-of-global-css-90d2a4a06284#.rl1wdxe16) which creates random id's

[Slides](http://slides.com/linclark/empirenode)



## Rapidly Iterating on Microservices using Docker and Node.js
- William Blankenship
- SourceNode - works on the docker images

DOCKER!
- addresses the pains of cat wrangling (?) and yak-shaving(?!)

* Don't use node for gzip/ssl type problems, use the server like nginx.

Dockerizing will be a challenge for most applications, but forces you to be more careful with your
init process. You should not have to touch db's or environment settings.

martinfowler.com
nodesource.com




## Building desktop apps with Node.js

We are here for Electron, what is it!? It's a tool for using web technology to make desktop apps - for example the Atom file editor. Allows you to build offline apps, shell apps, whatever. Slack uses it too.

You bundle a specific version of chromium into the build. 

npm install -g prebuilt

Can use the latest node and latest chromium!
Can use native os things like menu bars, dialogues, task bars etc...


## Node.js in the IOT
@nodebotanist - the@nodebotani.st
- Kassandra
- boucoup
Thin clients - do almost everything server side
demo of how we can use [electric imp](https://electricimp.com/) and [Particle Photon](https://store.particle.io/)
Plenty of opportunities to contribute, writing unit tests, docs or tutorials




## Refactoring the Dinosaur
- Suz Hinton [@noopkat](twitter.com/noopkat)
- kickstarter

Writing hardware apps (ie, applications to control a device programmer) is out of date. She goes through her process of updating it using [NW](http://nwjs.io/).



## The Social Coding Contract
- Justin Searls @searls

Companies can help each other succeed
Is open source good?

Unintended consequences - is amazon shipping goods close to you before you purchase it?

Dependency management - it's gotten easy to consume them. like commodities, they got easier to consume over time.
 - always more convenience! short term convenience in exchange for long term fragility. 
 - it allows you to use other peoples code that we don't know

It's never been easier to ship code, but our shipped code has never been more complex.

"make an empty project, wait a year, update, it'll break"

There is a maintener <----> early-adopter relationship
late-adopters remove the fun of the maintainer!

The more people you trust, the more people you don't even realize you trust!
Recognize when projects are marketing to you.
the move of opensource has been making adoption easier and easier

async chat - realtime chat - phone call - video chat - real life

https://www.nitrous.io/app/#/containers/new

***Adopting a dependency outsources our ability to understand a task***
It incurs an "understanding" debt, which is unacceptable for embedded systems.

