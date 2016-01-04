var path = require("path");

module.exports = {
    entry: ['./src/test.js'],
    loaders: [
        {
            loader: "babel-loader",

            // Skip any files outside of your project's `src` directory
            include: [
                path.resolve(__dirname, "src"),
            ],

            // Only run `.js` and `.jsx` files through Babel
            test: '.js',

            // Options to configure babel with
            query: {
                plugins: ['transform-regenerator'],
                presets: ['es2015']
            }
        },
    ]
}