var arDrone = require('ar-drone');
var _ = require('underscore');

// Connect to drone
var client = arDrone.createClient();

// This resets it after a crash
client.disableEmergency();

var State = {
    lastCommand :'none'
};


// Keep the drone between MIN and MAX height in meters
//  accelerating at a speed of x percent max (0 to 1.0)
var SPEED = 0.5;
var TARGET_MIN = 1;
var TARGET_MAX = 2;

/*
    // Contents of navdata event
    {
        header,
        droneState,
        sequenceNumber,
        visionFlag,
        demo : {
            controlState,
            altitude
        },
        visionDetect
    }
 */

function printAltitude(e) {
    var data = e && e.demo && e.demo.altitude;
    // Only show changes in data
    if (State.lastData === data) {
        return;
    }
    State.lastData = data;
    console.log('altitude : '+data);
}

function action(a, arg) {
    if (State.lastCommand === a && State.lastArgs === arg) {
        return;
    } else {
        console.log('executing ' + a);

        State.lastCommand = a;
        State.lastArgs = arg;
        client[a](arg);
    }
}

var controlLoop = function(e) {
    printAltitude(e);

    if (!e.demo) {
        console.log('No demo data returned');
        return;
    }

    var altitude = e.demo.altitudeMeters;

    if (altitude < TARGET_MIN) {
        action('up', SPEED);
    } else if (altitude > TARGET_MAX ) {
        action('down', SPEED);
    } else {
        action('stop');
    }
};
var loop = _.throttle(controlLoop, 100);


// Listen and launch!
client.on('navdata', loop);
action('takeoff');

// Shut down after 10 seconds
setTimeout(function() {
    action('stop');
    action('land');
    client.removeListener('navdata', loop);
}, 10*1000);
