// Challenge: Given a safe json type object, iterate through it
//  returning the total number of objects in it

function countDicts(obj) {
    var isArray = Array.isArray(obj);
    // Note that null items in javascript have a type of "object"
    var isObject = typeof obj === 'object' && obj !== null;

    var count;
    if (isArray) {
        count = 0;
    } else if (isObject) {
        count = 1;
    } else {
        return 0;
    }

    for (var x in obj) {
        // objects will iterate by key; arrays will iterate by index
        count += countDicts(obj[x])
    }
    return count;
}


function _runTest(obj, expected) {
    if (countDicts(obj) !== expected) {
        throw "Unexpected result"
    }
}

function test() {
    _runTest({}, 1);
    _runTest([], 0);
    _runTest([{}], 1);
    
    _runTest({
        a: "b",
        c: [{
            d: "e",
            f: {
                g: "h",
                z: [1, null, "zz", undefined]
            }
        },
        "i"
        ],
        "j": { } 
    }, 4);
}


test();
