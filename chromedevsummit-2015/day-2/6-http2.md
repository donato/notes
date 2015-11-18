# HTTP/2 101
Surma
@surmair

## H2 101
 * They call it "H2"
 * tldr - switch
 * Free performance boost, just enable it!
 
 
## Flaws in HTTP1
 * HOL blocking (head of line)
     - only 2 connections at a time, then 2
 * Meta data
     - You can gzip data but not headers
 
## What is H2 Really?
 * Overview
     - All requests begin as H1, but get upgraded to H2 if it works
     - A single TLS encrypted connection
     - Client can weight streams for which is more important, or which depends on what
 * Header Frames
     - Have a compression exclusively for headers "HPACK"
     - It works on the whole stream instead of a single header
     - Uses a dynamic huffman encoding which grows as you send packets
     - **This negates sharding and multi-origin cdn's**
     - unchanging cookies becomes highly compressable
 * Data Frames
     - ?
 * Push
     - The server can push the needed resources at once instead of waiting for the client to ask for it
 * Still need to use gzip, cdns, cache-control
 
## Today?
 * Yea!
 * jk, but put your static assets onto an H2 CDN
 * or tier 2 is to put a reverse proxy for H2 between app and client
