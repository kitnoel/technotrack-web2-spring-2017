/**
 * Created by lekse on 01.07.17.
 */
const webpack = require('webpack');
const BundleTracker  = require('webpack-bundle-tracker');

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: {
      app: './index.jsx',
    },
    context: `${__dirname}/static_src`,
    output: {
        path: `${__dirname}/static/build`,
        filename: 'indexBundle.js',
        publicPath: 'static/build/',
    },
    watch: true,
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: `${__dirname}/static_src`,
                loaders: [
                    // 'react-hot-loader',
                    'babel-loader?presets[]=react&presets[]=es2015&presets[]=stage-1',
                ]
            },
        ]
    },
    plugins: [
        new BundleTracker({ filename: './webpack-stats.json'})
    ]
};