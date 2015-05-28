# Mutations and Subscriptions in Relay - Laney Kuenzel
Cool library that no one can use, but we can all learn from

[Slides here](https://speakerdeck.com/laneyk/mutations-in-relay)

### Why?
* There is typically a coupling of defining what you expose on server and what you want on client
* Constantly fetching too much or too little
* "Under fetching" "over fetching"
* Keep logic for data fetching, and the rendering together - inside of a component
* A relay component has two pieces
    - Query - what to fetch - this is where you declare your data requirements
    - Render - how to draw

### FQL
* stands for facebook query language
* searches graph

### Relay 
* Seems like netflix's Falcor
* It is a "store" in a flux app
* A relay app has only one store

### Use case
1. In a comment stream, you currently get text only. Suppose you want to add "sticker" as well.
With relay, you would define a change in the Query and the Render, and everything else JUST WORKS

2. Suppose in a comment stream you want actions, for example adding a comment or liking something
 * We call these actions "mutations"
 * Past Strategy - write js, hit a custom endpoint, receive a response, update the DOM
 * Problem - each mutation used a custom endpoint, because it is repetitive and error prone
 * New Strategy - need a very structured API for writes
    - The response holds what? a boolean? an ID? everything?
    - Ideally we return the relevant updated data
 * Alternate motivating example
    - Suppose you want to add profile pics for people who liked a comment? Then you want to remove it again?

### Mutations
* Relay uses a mutation framework for writes
    - attrs : Type, Inputs, Query
    
* A defined mutation also contains a set of data which CAN POSSIBLY change as a result of the mutation
    - danger is over fetching
    - so relay creates a query which is the intersection of what the feature requires with what can possibly change
    
### Optimistic mutations and queing
* Fake writes to make it look responsive?
    - optimacy? an optimistic payload that guesses the correct response *IMPORTANT!*
        + For example after pressing "like" it blue thumbs and increments the count
    - This is called an optimistic update, using optimistic data
        + For example, I press play, but it hasn't begun playing
    - This works by maintaining a queue of "inflight data" which hasn't returned yet
        + a Mutation Queue, it doesn't update the queue , but does update the view!
        + A queue can go to error state, or remove/disappear
    - Detect dependancy between queued mutations (HOW?) and only allow one to be in flight at a time
    
### Subscriptions
* A way to have a component listen for relevant changes from the Store
* Essentially data binding
* By centralizing it, you only have to do it once, in one spot
