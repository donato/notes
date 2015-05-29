var arDrone = require('ar-drone');

// Connect to drone
var client = arDrone.createClient();

// This resets it after a crash
client.disableEmergency();

// Create Repl
client.createRepl();