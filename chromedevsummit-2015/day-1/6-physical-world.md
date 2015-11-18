# Engaging with the Real World: Web Bluetooth and Physical Web
Scott Jenson & Vincent Scheib

## Barriers
1. Needing to install an app
1. Had to join a wireless network
1. Slow website interaction

## Web Bluetooth
Connect to bluetooth devices from a website

Example heart rate monitor

+ Heart Rate device
++ Heart Rate Service
+++ Body sensor location
++++ value 1, value 2
+++ Heart rate Measurment
+++ Battery Service


```js
// Promise based
navigator.bluetooth.requestDevice({
    filters:[{
        services: ['battery_service']
    }]
}).then( ... )
```

## The Physical Web
The location bar is out-of-date!
Maybe a discovery service that can find urls for us

The new big thing is BLE - bluetooth low energy
Get's you from a device to a webpage as quickly as possible

Need some rules
1. just a webpage
1. only the link if they ask
1. only 

Solve two problems, spam via a filtering proxy

Eddystone - Googles broadcas format
UID TLM URL

Cloud passthrough

http://github.com/google/physical-web

