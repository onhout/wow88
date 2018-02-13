const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    context: __dirname,

    entry: {
        main: ['main/js/main', 'main/scss/main.scss'],
        user: ['user/js/user', 'user/scss/user.scss'],
        investors: ['investors/js/investors', 'investors/scss/investors.scss'],
        sales: ['sales/js/sales', 'sales/scss/sales.scss'],
        vendor: [
            'jquery',
            'jquery.easing',
            'popper.js',
            'bootstrap',
            'bootstrap-switch',
            'magnific-popup',
            'moment',
            'globals/creative.js',
            'globals/index.js',
            'globals/index.scss'
        ]
    }, // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

    output: {
        path: path.resolve('./static/dist/'),
        publicPath: '/static/dist/',
        chunkFilename: '[id]-[hash].chunk.js',
        filename: "[name]-[hash].js",
    },

    plugins: [
        // new webpack.optimize.UglifyJsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.ProvidePlugin({
            $: 'jquery',             // bootstrap requires
            jQuery: 'jquery',
            Popper: ['popper.js', 'default'],      // bootstrap requires
            moment: 'moment',
            ScrollReveal: 'scrollreveal',
        }),
        new ExtractTextPlugin('[name]-[hash].css'),
        new webpack.optimize.CommonsChunkPlugin({name: 'vendor', filename: 'vendor-[hash].js', Infinity}),
    ],

    devtool: 'cheap-module-source-map',

    module: {
        rules: [
            {test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
            {
                test: /\.(sass|scss)$/,
                loader: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader!sass-loader!resolve-url-loader!sass-loader?sourceMap"
                })
            }, //to transform less into CSS
            {test: /\.(jpe|jpg|png|woff|woff2|eot|ttf|gif|svg)(\?.*$|$)/, loader: 'url-loader?limit=100000'},//changed the regex because of an issue of loading less-loader for font-awesome.
            {test: /\.css$/, loader: ExtractTextPlugin.extract({fallback: "style-loader", use: "css-loader"})},
        ],
    },

    resolve: {
        modules: [
            path.resolve('./src'),
            './node_modules'
        ],
        extensions: ['.js', '.jsx']
    },
};