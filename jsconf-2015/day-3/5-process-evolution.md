# Evolution of Computational Processes

### Data in JS
* Mutable state is odd when shared between different processes
* So we have two ways to solve this problem
    - HAMT - Hash array mapped trie
    - For the purpose of this demo, we are visualizing the data structures of the storage
       for two different libraries which use HAMT
    - You can see a massive difference between how they handle queues by visualizing the data
    - when visualizing storage of hashes, banding indicates problems
    - immutable.js - 
    - Mori.js
* We can come to conclusions about code based off it's performance without actually looking at the code
    - This is important if code is obfuscated, or perhaps there is too much to go into
    
### How to Visualize
* Tinker with granularity
    - spatial
        + Between a single line and the entire code base
    - temporal
        + A single operation vs real time linearly
    - Memory
        + A single datum vs the entire heap
        + A current snapshot vs past/present/future
        
### Building a visualization
* homoiconicity - data and program are same type (like functional languages)
* fondue - instrumentation library
* visualize the code as it's running 
    - Allows you to build your intuition
