/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        str = "Hello World";
        return str;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */