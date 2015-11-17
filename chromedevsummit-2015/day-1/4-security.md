# Deploying HTTPS: the green lock and beyond
Emily Stark
From the Chrome Security Team

"Freedom massage by the TSA"

## Properties
 * can't be eavesdropped on
 * can't tamper or change the data, like adding new ads
 * can't impersonate others

**or else**
 * Blocked from more powerful features like camera or microphone

 * **It's not that hard**, try SSLMate

## Learn more
 1. Understanding lock Icon
    * Neutral state - no indication of security
    * In the future neutral will be negative! Https is the norm
    * Green - connection is secure
    * Neutral but https - there are problems with your security state
    * Red - certificate is expired or incorrect, or something bad
    
There will be a new panel in Dev Tools to help you audit your security state (try it in Canary)
email estark@chromium.org with questions

 1. Getting to the green
    * Could be problems with mixed content
    * You may get the green, but then if you click the shield and enable stuff, it'll go red
    * You can tinker with the headers for the page "Content-Security-Policy"
    * report-uri.io - when a user gets mixed content, analyze the reports of it here
    
 1. Beyond the green
    * set-cookie should be Secure!
    * strict-transport-security: max-age=9999999; includeSubDomains
    * If any root CA goes evil, they can issue fake certificates for your website "misissued certs"
        - solution 1: Certificate transparency - easy to monitor all certs and catch bad ones
        - solution 2: public key pinning - let the site tell client what the cert chain should look like
            for now this is easy to mess up, so google made a "practice mode" using mismatch reporting
