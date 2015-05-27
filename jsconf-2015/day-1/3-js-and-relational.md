# JS on ACID - Tim Griesser
Relational DBs are great, how can we make JS environment more hospitable?

    A - atomicity
    C - consistency
    I - isolation
    D - durability

* Databases are static and strongly typed
* JS is loosely typed (0.1 + 0.2)
* SQL will never die
* Maybe the movement against sql was cultural - people rebelling against traditional models
    - Lebron stack! - it's a slam dunk
    - people start to believe that relational dbs are the enemy, and not suited for node.js
* Node lacks a common DB API - so clients of mysql vs postgres vs etc.. are different
    - mix of ORM layer/query layer
    - no transaction API?

### Tools
* Knex
    - meant to be the lower level
    - standardize the inconsistencies between relational dbs
    - chain the queries instead of concatting strings select('*').from('').where('').then(fn(){});
* Bookshelf
    - ORM - object relational mapper for relational
    - fetch, fetchAll, save, destroy
    - can use knex, but (maybe) doesn't need to , allowing a separation

